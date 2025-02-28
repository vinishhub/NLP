#pip install gensim
from gensim.utils import tokenize
str = "I love to study Natural Language Processing in Python"
print(list(tokenize(str)))
