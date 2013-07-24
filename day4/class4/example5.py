# Using an external data cleaning function
dataiap_home = '../../dataiap/'

import os, sys, math
sys.path.append(dataiap_home+'resources/util') # fix this path to work for you!!!!
from email_util import *
sys.path.append(dataiap_home+'day4/') # fix this path to work for you!!!!
from get_terms import *
from collections import Counter, defaultdict

# TF
folder_tf = defaultdict(Counter)

for e in EmailWalker(sys.argv[1]):
    terms_in_email = get_terms(e['subject']) # cleans the data for us
    folder_tf[e['folder']].update(terms_in_email)

#print terms_in_email[:100]

# IDF ?
terms_per_folder = defaultdict(set)
allterms = Counter()
nemails = 0
for e in EmailWalker(sys.argv[1]):
    terms_in_email = get_terms(e['subject']) # cleans the data for us
    # this collects all of the terms in each folder
    terms_per_folder[e['folder']].update(terms_in_email)

for folder, terms in terms_per_folder.iteritems():
    # this will increment the counter value for each term in `terms`
    allterms.update(terms)

idfs = {}
nfolders = len(terms_per_folder)
for term, count in allterms.iteritems():
    idfs[term] = math.log( nfolders / (1.0 + count) )

tfidfs = defaultdict(list) # key is folder name, value is a list of (term, tfidf score) pairs

# write code to calculate tf-idfs yourself!
for folder, tfs in folder_tf.iteritems():
    for term, freq in tfs.iteritems():
        pair = (term, freq * idfs[term])            
        tfidfs[folder].append(pair)

for folder, terms in tfidfs.items():
    print folder
    sorted_by_count_top20 = sorted(terms, key=lambda (k,v): v, reverse=True)[:20]
    for pair in sorted_by_count_top20:
        print '\t', pair