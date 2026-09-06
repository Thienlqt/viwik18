from gensim.models import Word2Vec
from gensim.models import KeyedVectors

model = Word2Vec.load("models/cbow/word2vec_cbow.model")
word_vectors = model.wv
word_vectors.save("models/cbow/word2vec_cbow.wordvectors")
wv = KeyedVectors.load("models/cbow/word2vec_cbow.wordvectors", mmap='r')
while (True):
    print("-"*25)
    print("Find most similar words")
    print("-"*25)
    user_input = input("Please input a word: ")

    if user_input.lower() == "q" or user_input.lower() == "quit":
        break

    vector = wv[user_input]  # get numpy vector of a word
    sims = wv.most_similar(user_input, topn=50)  # get other similar words

    print(f"Shape of the word embeddings: {vector.shape}")
    print(vector[:100])
    print("\n")
    print(f"Similar words: \n{sims}\n")
