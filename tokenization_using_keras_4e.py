import keras
from tensorflow.keras.preprocessing.text import text_to_word_sequence
str = "I love to study Natural Language Processing in Python"
tokens = text_to_word_sequence(str)
print(tokens)
