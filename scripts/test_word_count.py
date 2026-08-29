import nltk
from collections import defaultdict

try:
    nltk.data.find('corpora/words')
except LookupError:
    nltk.download('words')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

from nltk.corpus import words, wordnet

def test_words():
    english_words = set(w.lower() for w in words.words() if w.isalpha() and len(w) >= 2)
    # also add all wordnet lemmas
    for syn in wordnet.all_synsets():
        for lem in syn.lemma_names():
            lem_clean = lem.lower().replace('_', ' ')
            if lem_clean.isalpha() and len(lem_clean) >= 2:
                english_words.add(lem_clean)
                
    print(f"Total unique words collected: {len(english_words)}")
    
    by_letter = defaultdict(list)
    for w in english_words:
        by_letter[w[0]].append(w)
        
    for c in 'abcdefghijklmnopqrstuvwxyz':
        print(f"Letter '{c.upper()}': {len(by_letter[c])} words available")

if __name__ == '__main__':
    test_words()
