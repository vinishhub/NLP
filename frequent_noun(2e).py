import nltk
from collections import defaultdict
nltk.download('averaged_perceptron_tagger')
text=nltk.word_tokenize("Nick Likes toplay Football.Nick does not like to play cricket.")
tagged=nltk.pos_tag(text)
print(tagged)


addNounWords=[]
count=0
for words in tagged:
 val = tagged[count][1]
 if(val == 'NN' or val == 'NNS' or val == 'NNPS' or val == 'NNP'):
    addNounWords.append(tagged[count][0])
    count+=1
print (addNounWords)
temp = defaultdict(int)
for sub in addNounWords:
 for wrd in sub.split():
     temp[wrd] += 1
res = max(temp, key=temp.get)
print("Word with maximum frequency : " + str(res)) 
