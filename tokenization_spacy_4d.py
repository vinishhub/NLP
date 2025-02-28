import spacy
nlp = spacy.blank("en")
str = "I love to study Natural Language Processing in Python"
doc = nlp(str)
words = [word.text for word in doc]
print(words)
