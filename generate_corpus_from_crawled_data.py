more_stopWords = ["A","a's","a","able","about","above","according","accordingly","across","actually","after","afterwards","again","against","ain't","all","allow","allows","almost","alone","along","already","also","although","always","am","among","amongst","an","and","another","any","anybody","anyhow","anyone","anything","anyway","anyways","anywhere","apart","appear","appreciate","appropriate","are","aren't","around","as","aside","ask","asking","associated","at","available","away","awfully","b","be","became","because","become","becomes","becoming","been","before","beforehand","behind","being","believe","below","beside","besides","best","better","between","beyond","both","brief","but","by","c","c'mon","c's","came","can","can't","cannot","cant","cause","causes","certain","certainly","changes","clearly","co","com","come","comes","concerning","consequently","consider","considering","contain","containing","contains","corresponding","could","couldn't","course","currently","d","definitely","described","despite","did","didn't","different","do","does","doesn't","doing","don't","done","down","downwards","during","e","each","edu","eg","eight","either","else","elsewhere","enough","entirely","especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","exactly","example","except","f","far","few","fifth","first","five","followed","following","follows","for","former","formerly","forth","four","from","further","furthermore","g","get","gets","getting","given","gives","go","goes","going","gone","got","gotten","greetings","h","had","hadn't","happens","hardly","has","hasn't","have","haven't","having","he","he's","hello","help","hence","her","here","here's","hereafter","hereby","herein","hereupon","hers","herself","hi","him","himself","his","hither","hopefully","how","howbeit","however","i","i'd","i'll","i'm","i've","ie","if","ignored","immediate","in","inasmuch","inc","indeed","indicate","indicated","indicates","inner","insofar","instead","into","inward","is","isn't","it","it'd","it'll","it's","its","itself","j","just","k","keep","keeps","kept","know","knows","known","l","last","lately","later","latter","latterly","least","less","lest","let","let's","like","liked","likely","little","look","looking","looks","ltd","m","mainly","many","may","maybe","me","mean","meanwhile","merely","might","more","moreover","most","mostly","much","must","my","myself","n","name","namely","nd","near","nearly","necessary","need","needs","neither","never","nevertheless","new","next","nine","no","nobody","non","none","noone","nor","normally","not","nothing","novel","now","nowhere","o","obviously","of","off","often","oh","ok","okay","old","on","once","one","ones","only","onto","or","other","others","otherwise","ought","our","ours","ourselves","out","outside","over","overall","own","p","particular","particularly","per","perhaps","placed","please","plus","possible","presumably","probably","provides","q","que","quite","qv","r","rather","rd","re","really","reasonably","regarding","regardless","regards","relatively","respectively","right","s","said","same","saw","say","saying","says","second","secondly","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sensible","sent","serious","seriously","seven","several","shall","she","should","shouldn't","since","six","so","some","somebody","somehow","someone","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specified","specify","specifying","still","sub","such","sup","sure","t","t's","take","taken","tell","tends","th","than","thank","thanks","thanx","that","that's","thats","the","their","theirs","them","themselves","then","thence","there","there's","thereafter","thereby","therefore","therein","theres","thereupon","these","they","they'd","they'll","they're","they've","think","third","this","thorough","thoroughly","those","though","three","through","throughout","thru","thus","to","together","too","took","toward","towards","tried","tries","truly","try","trying","twice","two","u","un","under","unfortunately","unless","unlikely","until","unto","up","upon","us","use","used","useful","uses","using","usually","uucp","v","value","various","very","via","viz","vs","w","want","wants","was","wasn't","way","we","we'd","we'll","we're","we've","welcome","well","went","were","weren't","what","what's","whatever","when","whence","whenever","where","where's","whereafter","whereas","whereby","wherein","whereupon","wherever","whether","which","while","whither","who","who's","whoever","whole","whom","whose","why","will","willing","wish","with","within","without","won't","wonder","would","would","wouldn't","x","y","yes","yet","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves","z","zero"]

def print_Document_Set(doc_set):
	i=1
	for d in doc_set:
		print "Document ", i, ": ", d, "\n"
		i+=1

def stem_Document_Set(stopped_tokenized_doc_set):
	stemmed_stopped_tokenized_doc_set = []
	from nltk.stem.porter import PorterStemmer

	#create an object p_stemmer of class PorterStemmer
	p_stemmer = PorterStemmer()
	for stop_tok_d in stopped_tokenized_doc_set:
		#stem the list of all tokens
		stemmed_stopped_tokenized_doc_set.append([p_stemmer.stem(w) for w in stop_tok_d])
	return stemmed_stopped_tokenized_doc_set

def tokenize_Document_Set(doc_set):
	tokenized_doc_set = []
	from nltk.tokenize import RegexpTokenizer
	tokenizer = RegexpTokenizer(r'\w+')
	for d in doc_set:
		lower_d = d.lower()
		tokenized_doc_set.append(tokenizer.tokenize(lower_d))
	return tokenized_doc_set

def run_through_POS_tagger(tokenized_doc_set):
	noun_adjective_doc_set = []
	from nltk import pos_tag
	for doc_1 in tokenized_doc_set:
		POS_tagged_tuple_list = pos_tag(doc_1)	
		noun_adjective_doc = [w for (w,tag) in POS_tagged_tuple_list if tag in ['NN','NNP','NNS','NNPS','JJ','JJR','JJS'] ]
		#print "NN JJ doc : " , noun_adjective_doc
		noun_adjective_doc_set.append(noun_adjective_doc)
	
	return noun_adjective_doc_set

def removeStopWords_from_Document_Set(tokenized_doc_set):
	stopped_tokenized_doc_set = []
	from stop_words import get_stop_words

	#fetch the list of all the English stop words
	en_stop = get_stop_words('en')
	en_stop = [word.encode('ascii') for word in en_stop]

	for tok_d in tokenized_doc_set:
		#remove stop words from the tokenized_document tok_d

		to_append = []

		for w in tok_d:
			try:
				if not w in byteify(en_stop) and not w.isdigit() and len(w) > 3 and not w in more_stopWords:
					w = unicode(w, errors='replace')
					to_append.append(w)
			except:
				continue

		stopped_tokenized_doc_set.append(to_append)

	return stopped_tokenized_doc_set


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

'''
gensim --> dictionary API :

filter_extremes(no_below=5, no_above=0.5, keep_n=100000)
Filter out tokens that appear in

less than no_below documents (absolute number) or
more than no_above documents (fraction of total corpus size, not absolute number).
after (1) and (2), keep only the first keep_n most frequent tokens (or keep all if None)
'''

def construct_Dictionary(cleaned_doc_set):
	from gensim import corpora, models
	dictionary = corpora.Dictionary(cleaned_doc_set)
	#dictionary.filter_extremes(no_above=0.8)
	return dictionary

def construct_Bag_of_Words_Corpus(dictionary,cleaned_doc_set):
	corpus = [dictionary.doc2bow(d) for d in cleaned_doc_set]
	return corpus

import json
from gensim import corpora, models
import cPickle



print "Populating the document set...\n"

#with open('scholars-data.json') as json_file:
#with open('trial_data.json') as json_file:
with open('authstring1') as f:
    content = f.readlines()

_scholID_to_counter_map_ = {}

_doc_set_for_LDA_ = []

counter = 0;

for line in content:

	#scholID = int(byteify(record['scholar-id']))
	split_line = line.split(':',1)

	if len(split_line[1].strip(' ')) < 2:	# continue if no content in author - document string
		continue

	scholID = int(split_line[0])

	_scholID_to_counter_map_[scholID] = counter

	_doc_set_for_LDA_.append(split_line[1])	
	counter+=1


print "\nCleaning the document set..."
#print_Document_Set(_doc_set_for_LDA_)
print "		Tokenizing..."
_doc_set_for_LDA_ = tokenize_Document_Set(_doc_set_for_LDA_)
#print_Document_Set(_doc_set_for_LDA_)
#print "		POS Tagging..."
#_doc_set_for_LDA_ = run_through_POS_tagger(_doc_set_for_LDA_)
#print_Document_Set(_doc_set_for_LDA_)
print "		Removing Stop Words..."
_doc_set_for_LDA_ = removeStopWords_from_Document_Set(_doc_set_for_LDA_)
#print_Document_Set(_doc_set_for_LDA_)
#print "		Stemming..."
#_doc_set_for_LDA_ = stem_Document_Set(_doc_set_for_LDA_)
_doc_set_for_LDA_ = byteify(_doc_set_for_LDA_)

### Now the document set has been cleaned and is ready for generating the LDA model

#for key,value in _scholID_to_counter_map_.iteritems() :
#	print "scholar-id : " , key , " 	counter : " , value , "\n  doc_text : \n" , _doc_set_for_LDA_[value] , "\n\n"


print "Populating Dictionary out of the cleaned set...\n"
dictionary = construct_Dictionary(_doc_set_for_LDA_)	
print "Dictionary has been populated !\n Generating Bag of Words Corpus ...\n"		
corpus = construct_Bag_of_Words_Corpus(dictionary,_doc_set_for_LDA_)
print "BOW Corpus generated !\n\n"

cPickle.dump(_doc_set_for_LDA_, open('training_document_set.p', 'wb')) 
cPickle.dump(corpus, open('training_corpus.p', 'wb')) 
cPickle.dump(dictionary, open('training_dictionary.p', 'wb')) 
cPickle.dump(_scholID_to_counter_map_, open('scholID_to_counter_map.p', 'wb')) 

print "The generated corpus and dictionary has been saved to training_corpus.p and training_dictionary.p \n"
