import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = 'C:\\Users\\Vinish\\Downloads\\NLP-20250228T164512Z-001\\NLP'
filelist = PlaintextCorpusReader(corpus_root, '.*',encoding='latin1')
print ('\n File list: \n')
print (filelist.fileids())
print (filelist.root)
print ('\n\nStatistics for each text:\n')
print('AvgWordLen\tAvgSentenceLen\tno.ofTimesEachWordAppearsOnAvg\tFileName')
for fileid in filelist.fileids():
    num_chars = len(filelist.raw(fileid))
    num_words = len(filelist.words(fileid))
    num_sents = len(filelist.sents(fileid))
    num_vocab = len(set([w.lower() for w in filelist.words(fileid)]))
    print (int(num_chars/num_words),'\t\t\t', int(num_words/num_sents),'\t\t\t',
int(num_words/num_vocab),'\t\t', fileid)
