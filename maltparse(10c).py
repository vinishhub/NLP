from nltk.parse import malt
mp = malt.MaltParser('C:\\Users\\Vinish\\Downloads\\maltparser-1.7.2', 'C:\\Users\\Vinish\\Downloads\\engmalt.linear-1.7.mco')#file
t = mp.parse_one('I saw a bird from my window.'.split()).tree()
print(t)
t.draw()
