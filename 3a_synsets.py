import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
print(wordnet.synsets("computer"))
print(wordnet.synset("computer.n.01").definition())
print("Examples:", wordnet.synset("computer.n.01").examples())
print(wordnet.lemma('buy.v.01.buy').antonyms())
