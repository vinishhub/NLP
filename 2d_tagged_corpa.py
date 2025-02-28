import nltk
from nltk import tokenize
nltk.download('punkt')
nltk.download('words')
para = "Calling the recognize_google() method (or another available recognition method) on the SpeechRecognition library to convert the audio data into text."
sents = tokenize.sent_tokenize(para)
print("\nsentence tokenization\n===================\n",sents)

print("\nword tokenization\n===================\n")
for index in range(len(sents)):
 words = tokenize.word_tokenize(sents[index])
 print(words) 
