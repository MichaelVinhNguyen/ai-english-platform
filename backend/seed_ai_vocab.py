import asyncio
import os
import json
import sys
from pathlib import Path

# Add root to sys.path
sys.path.append(str(Path(__file__).parent.parent))

from backend.config import settings
from backend.database.database import AsyncSessionLocal, engine, Base
from backend.database.models import Vocabulary
from google import genai
from pydantic import BaseModel

# Initialize GenAI client
client = genai.Client(api_key=settings.GEMINI_API_KEY)

class WordResponse(BaseModel):
    word: str
    ipa: str
    word_type: str
    definition_en: str
    definition_vi: str
    level: str
    topic: str

class BatchResponse(BaseModel):
    words: list[WordResponse]

async def seed_letter(letter: str, count: int = 150):
    # Reduced to 150 per prompt to prevent JSON truncation issues, will run twice for 300
    print(f"[START] Generating {count} words for letter '{letter}'...")
    prompt = f"Generate exactly {count} distinct and common English vocabulary words starting with the letter '{letter}'. Provide word, ipa, word_type, definition_en, definition_vi, level (A1-C2), and topic. Output strictly JSON matching the schema."
    
    try:
        response = await client.aio.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": BatchResponse,
                "temperature": 0.5
            }
        )
        
        data = json.loads(response.text)
        words_list = data.get("words", [])
        
        async with AsyncSessionLocal() as session:
            for w in words_list:
                vocab = Vocabulary(
                    word=w["word"],
                    ipa=w["ipa"],
                    word_type=w["word_type"],
                    definition_en=w["definition_en"],
                    definition_vi=w["definition_vi"],
                    level=w["level"],
                    topic=w["topic"]
                )
                session.add(vocab)
            await session.commit()
            print(f"[SUCCESS] Letter '{letter}': Inserted {len(words_list)} words.")
    except Exception as e:
        print(f"[ERROR] Letter '{letter}': {e}")

async def process_letter_full(letter: str):
    # Two passes to get roughly 300 words
    await seed_letter(letter, 150)
    await asyncio.sleep(2)
    await seed_letter(letter, 150)

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # To avoid rate limits, we process 2 letters concurrently
    for i in range(0, len(letters), 2):
        batch = letters[i:i+2]
        print(f"--- Processing batch: {batch} ---")
        await asyncio.gather(*(process_letter_full(l) for l in batch))
        await asyncio.sleep(5)
        
    print("[FINISHED] Vocabulary seeding complete!")

if __name__ == "__main__":
    asyncio.run(main())
