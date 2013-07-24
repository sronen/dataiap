# Reattribution to spouse:
# stored in fields "receipt_desc" and "memo_text"

# run on donations_obama_mccain.txt (or _sampled.txt)

from collections import defaultdict
import  matplotlib.pyplot as plt
import csv, sys, datetime

reader = csv.DictReader(open(sys.argv[1], 'r'))

for row in reader:
    receipt_desc = row['receipt_desc']
    memo_text = row['memo_text']    
    
    if 'SPOUSE' not in receipt_desc and 'SPOUSE' not in memo_text:
        # look for retributions only (in uppercase)
        continue
    
    print row