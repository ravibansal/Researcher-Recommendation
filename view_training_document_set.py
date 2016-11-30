import cPickle

print "\n Retrieving the saved document set from training_document_set.p ...\n"

doc_set = cPickle.load(open('../training_document_set.p', 'rb'))
_scholID_to_counter_map_ = cPickle.load(open('../scholID_to_counter_map.p','rb'))

for key,value in _scholID_to_counter_map_.iteritems():
	print "Scholar-ID" , key , "	 Document Text :  " , doc_set[value]

