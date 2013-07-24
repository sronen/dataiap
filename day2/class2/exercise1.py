#Many people say that Obama was able to attract votes from "the common man", and had far more smaller contributions that his competitors. Let's plot a histogram of each candidate's contribution amounts in $100 increments to see if this is the case

from collections import defaultdict
import  matplotlib.pyplot as plt
import csv, sys, datetime
import math

bucket_size = 100

reader = csv.DictReader(open(sys.argv[1], 'r'))

obamadonations = defaultdict(lambda:0)
mccaindonations = defaultdict(lambda:0)

# classify donations into buckets.

for row in reader:
    name = row['cand_nm']
    amount = float(row['contb_receipt_amt'])

    k = int( math.floor(amount/bucket_size) * bucket_size ) # sort into the right bucket. To round to nearest hundred use: k = int(round(amount, -2)) 

    # Classify to right candidate.
    # We ignore the outliers and focus on the majority of the data points. We only create histogram buckets within 3 standard deviations of the overall average donation.
    #For Obama, that's donations between [-$18000, $19000]. For McCain, that's between [-$22000, $22000]
    if 'Obama' in name and -18000 <= amount <= 19000:
        obamadonations[k] += 1
    if 'McCain' in name and -22000 <= amount <= 22000:
        mccaindonations[k] += 1

# dictionaries 
sorted_by_amount_obama = sorted(obamadonations.items(), key=lambda (key,val): key)
xs_obama,ys_obama = zip(*sorted_by_amount_obama) # zip(*x) unzips list x

sorted_by_amount_mccain = sorted(mccaindonations.items(), key=lambda (key,val): key)
xs_mccain,ys_mccain = zip(*sorted_by_amount_mccain)

# To easily offset McCain's bar, turn it into a numpy list, then add desired offset during plot
import numpy as np
xs_mccain = np.array(xs_mccain) # turn to a numpy list so we can offset easily later

width = bucket_size / 2.0 # need to fit two bars in each bucket. This will also be the offset for the second bar 

# matplotlib places the two seprate x-value lists on the same x-axis.
# Note that len(xs_?) must equal len(ys_?)
plt.bar(xs_obama, ys_obama, width=width, label='Obama\'s Donations', color='blue')
plt.bar(xs_mccain+width, ys_mccain, width=width, label='McCain\'s Donations', color='red') # added an offset equal to the width, to display candidate bars side-by-side for each bucket

plt.legend(loc='upper center', ncol = 4)
plt.savefig('test_obama_mccain.png', format='png')