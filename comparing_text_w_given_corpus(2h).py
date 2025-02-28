from __future__ import with_statement
import re
words = []
testword = []
ans = []
print("MENU")
print("-----------")
print(" 1 . Hash tag segmentation ")
print(" 2 . URL segmentation ")
print("enter the input choice for performing word segmentation")
choice = int(input())
if choice ==1:
    text="#whatismyname"
    print("input with HashTag",text)
    pattern=re.compile("[^\w']")
    a=pattern.sub('',text)
elif choice==2:
    text = "www.whatismyname.com" 
    print("input with URL",text)
    a=re.split('\s|(?<!\d)[,.](?!\d)', text)
    splitwords = ["www","com","in"]
    a ="".join([each for each in a if each not in splitwords])
else:
    print("wrong choice...try again")
print(a)

for each in a:
    testword.append(each) 
test_length = len(testword)

with open('Words.txt', 'r') as f:
    lines = f.readlines()
    words =[(e.strip()) for e in lines]


def Seg(a,length):
    ans=[]
    for k in range(0,length+1):
        if a[0:k] in words:
            print(a[0:k],"-appears in the corpus")
            ans.append(a[0:k])
            break
    if ans!=[]:
        g = max(ans,key=len)
        return g
test_tot_itr = 0 
answer = [] 
Score = 0
N = 37
M = 0
C = 0
while test_tot_itr < test_length:
    ans_words = Seg(a,test_length)
    if ans_words != 0:
        test_itr = len(ans_words)
    answer.append(ans_words)
    a = a[test_itr:test_length]
    test_tot_itr += test_itr
        
Aft_Seg = " ".join([each for each in answer])
print("output")
print("---------")
print(Aft_Seg)
C = len(answer)
score = C * N / N 
print("Score",score)



