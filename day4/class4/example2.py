# We can count the number of times each term occurs in each email, and the top occurrences of terms across all emails in each folder should best represent the folder
dataiap_home = '../../dataiap/'

import os, sys, math
sys.path.append(dataiap_home+'resources/util') # fix this path to work for you!!!!
from email_util import *
from collections import Counter, defaultdict

folder_tf = defaultdict(Counter)

# sys.argv[1] = ../../dataiap/datasets/emails/lay-k

for e in EmailWalker(sys.argv[1]):
    terms_in_email = e['text'].split() # split the email text using whitespaces
    folder_tf[e['folder']].update(terms_in_email)

for folder, counter in folder_tf.items():
    print folder
    sorted_by_count_top20 = sorted(counter.items(), key=lambda (k,v): v, reverse=True)[:20] # sort, using the value of dictionary entries (=number of occurences) as sort key
    for pair in sorted_by_count_top20:
        print '\t', pair