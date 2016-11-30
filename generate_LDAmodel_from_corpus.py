print "\n Retrieving the saved corpus and dictionary from training_corpus.p and training_dictionary.p ...\n"

import cPickle
corpus = cPickle.load(open('training_corpus.p', 'rb'))
dictionary = cPickle.load(open('training_dictionary.p', 'rb'))

#print "The following is the tokens' list, each against its unique dictionary ID :\n"
#print dictionary.token2id
#print "\nPrinting the document vectors of term-document pairs : \n\n"
#print_Document_Set(corpus)

print "Now, that we have our CORPUS and DICTIONARY, we are ready to begin constructing our LDA model..."
print "Please enter the number of topics to be generated, and the no. of passes/laps to iterate through the corpus: "
print "Please NOTE : The greater the number of passes, the more accurate the model will be. A lot of passes can be slow on a very large corpus."

num_topics_ = input("\n\nEnter No. of topics : ")
num_passes = input("\nEnter No. of passes : ")

print "\n\nConstructing the LDA model... \n"

from gensim import models

ldamodel = models.ldamodel.ldamulticore.LdaMulticore(corpus, num_topics = num_topics_, id2word = dictionary, passes = num_passes)

ldamodel.save('lda.model')

#print "Lda topic distribution for the 1st document : " , ldamodel[ dictionary.doc2bow(_doc_set_for_LDA_[0]) ]

print "The generated LDA model has been saved to lda.model \n"

