import nltk
from nltk.tokenize import RegexpTokenizer
tk = RegexpTokenizer('\s+', gaps = True)
str = "I love to study Natural Language Processing in Python"
tokens = tk.tokenize(str)
print(tokens)
