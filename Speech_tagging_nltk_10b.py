import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
nltk.download('state_union')
train_text = state_union.raw("C:\\Users\\Student\\Downloads\\2005-GWBush.txt")
sample_text = state_union.raw("C:\\Users\\Student\\Downloads\\2006-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)
def process_content():
    try:
        for i in tokenized[:2]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
        print(tagged)
    except Exception as e:
        print(str(e))

process_content()
