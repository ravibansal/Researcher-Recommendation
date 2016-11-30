
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

import cPickle

print "\n Retrieving the saved dictionary from training_dictionary.p ...\n"

dictionary = cPickle.load(open('../training_dictionary.p', 'rb'))

print "The following is the tokens' list, each against its unique dictionary ID :\n"
print byteify(dictionary.token2id)