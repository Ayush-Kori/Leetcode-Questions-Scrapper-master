# read the index.txt and prepare documents, vocab , idf

import chardet

def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encodeing']
    return charenc

filename = 'Scrapper Master/index.txt'
my_encoding = find_encoding(filename)

with open(filename,'r',encoding=my_encoding) as f:
    lines  = f.readlines()

def preprocess(document_text):
    #remove the loading numbers from the string, remove notalpha numeric characters. make everything lowercase
    terms = [term.lower() for term in document_text.strip().split()[1:]]
    return terms

vocab = {}
documents  = {}

for index, line in enumerate(lines):
    #read statements and add it to the line and then preprocess
    token   = preprocess(line)
    documents.appnd(tokens)
    tokens = set(tokens)
    for token in tokens:
        if token not in vocab:
            vocab[token]  = 1
        else:
            vocab[token] += 1


 # reverse sort the vocab by the values
 vocab = dict(sorted(vocab.items(),key-lambda item:item[1],reverse=True))
               
print('Number of documents', len(documents))
print('Size of vocab: ', len(vocab))
print('Sample document ', document[0])

# save the vocab in a text file
with open('tf-idf/vocab.txt', 'w') as f:
    for key in vocab.keys():
        f.write("%s\n" %vocab[key])

#save the documents in a text file 
with open('tf-idf/document.txt', 'w') as f:
    for document in documents:
        f.write("%s\n" % ' '.join(document))

inverted_index = {}
for index, document in enumerate(documents):
    for token in document:
        if token not in inverted_index:
            inverted_index[token] = [index]
        else
            inverted_index[token].append(index)

#save the inverted index in a text file
with open('tf-idf/inverted-index.txt', 'w') as f:
    for key in inverted_index.keys():
        f.write("%s\n" % key)
        f.write("%s\n" % ' '.join([str(doc_id) for doc_id in inverted_index[key]]))
