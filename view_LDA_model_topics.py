
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    elif isinstance(input, tuple) and len(input) == 2:
    	return (input[0], byteify(input[1]))
    else:
        return input



import json
from gensim import corpora, models

# later on, load trained model from file
print "\n Retrieving the saved LDA Model from lda.model...\n"
ldamodel =  models.LdaModel.load('../lda.model')


num_topics_ = input("\n\nEnter No. of topics : ")
num_words_ = input("\nEnter No. of words per topic : ")

print "Printing", num_topics_,"Topics @ ", num_words_ , " words per topic = " 

_list_ = ldamodel.print_topics( num_topics= num_topics_, num_words= num_words_)
_list_ = byteify(_list_)

i=0
for topic in _list_:
	print "Topic " , i , ": " , topic
	i+=1