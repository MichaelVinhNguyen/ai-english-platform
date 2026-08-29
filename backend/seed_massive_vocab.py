import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from collections import defaultdict
import concurrent.futures

from backend.database.database import AsyncSessionLocal, init_db
from backend.database.models import Vocabulary

try:
    from deep_translator import GoogleTranslator
except ImportError:
    GoogleTranslator = None

try:
    import nltk
    from nltk.corpus import words, wordnet
except Exception:
    nltk = None
    words = None
    wordnet = None

async def seed_vocab():
    print("[START] Seeding massive vocabulary...")
    await init_db()
    
    # Get all english words
    english_words = set(w.lower() for w in words.words())
    print(f"Total NLTK words: {len(english_words)}")
    
    # Group by first letter
    grouped = defaultdict(list)
    for word in english_words:
        if word.isalpha() and len(word) >= 3: # Ignore short words
            grouped[word[0]].append(word)
            
    # Select 300 words for each letter A-Z
    selected_words = []
    for char in 'abcdefghijklmnopqrstuvwxyz':
        words_for_char = sorted(grouped[char]) # Sort to get consistent results
        selected_words.extend(words_for_char[:300]) # Take first 300
        
    print(f"Selected {len(selected_words)} words to seed.")
    
    # We will use ThreadPoolExecutor to translate in parallel, but not too aggressively to avoid ban
    translator = GoogleTranslator(source='en', target='vi')
    
    def fetch_word_data(word):
        try:
            synsets = wordnet.synsets(word)
            if not synsets:
                return None
            
            synset = synsets[0]
            definition_en = synset.definition()
            pos = synset.pos()
            
            # Map POS
            pos_map = {'n': 'noun', 'v': 'verb', 'a': 'adjective', 'r': 'adverb', 's': 'adjective'}
            word_type = pos_map.get(pos, 'noun')
            
            examples = synset.examples()[:2]
            
            # Translate word
            meaning_vi = translator.translate(word)
            
            return {
                "word": word,
                "ipa": f"/{word}/", # Dummy IPA as NLTK doesn't provide it easily
                "word_type": word_type,
                "level": "B1", # Default level
                "topic": "General",
                "definition_en": definition_en,
                "definition_vi": meaning_vi,
                "examples": examples,
                "synonyms": [],
                "antonyms": []
            }
        except Exception as e:
            return None

    # Fetch data
    valid_data = []
    print("Fetching definitions and translating... (This will take a while)")
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(fetch_word_data, selected_words))
        
    for r in results:
        if r is not None:
            valid_data.append(r)
            
    print(f"Successfully processed {len(valid_data)} words.")
    
    # Insert to DB
    async with AsyncSessionLocal() as session:
        # Check if already seeded to prevent duplication
        # We check count
        result = await session.execute(select(Vocabulary))
        existing_count = len(result.scalars().all())
        if existing_count > 5000:
            print(f"Already have {existing_count} words in DB. Skipping massive seed.")
            return
            
        print("Inserting to database in batches...")
        batch_size = 500
        for i in range(0, len(valid_data), batch_size):
            batch = valid_data[i:i+batch_size]
            for item in batch:
                session.add(Vocabulary(**item))
            await session.commit()
            print(f"Inserted {i+len(batch)} / {len(valid_data)}")
            
    print("[DONE] Massive vocabulary seeded successfully.")

if __name__ == "__main__":
    asyncio.run(seed_vocab())
