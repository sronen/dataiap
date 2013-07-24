# Shows comulative donations to-date

from collections import defaultdict
import  matplotlib.pyplot as plt
import csv, sys, datetime

reader = csv.DictReader(open(sys.argv[1], 'r'))

obamadonations = defaultdict(lambda:0)
mccaindonations = defaultdict(lambda:0)

for row in reader:
    name = row['cand_nm']
    datestr = row['contb_receipt_dt']
    amount = float(row['contb_receipt_amt'])
    date = datetime.datetime.strptime(datestr, '%d-%b-%y')

    if 'Obama' in name:
        obamadonations[date] += amount
    elif 'McCain' in name:
        mccaindonations[date] += amount

# dictionaries: create a sorted list from dictionary, then calculate 
# the comulative donations for each date
sorted_by_date_obama = sorted(obamadonations.items(), key=lambda (key,val): key)

obama_to_date = 0
for i in range( len(sorted_by_date_obama) ):
    obama_to_date += sorted_by_date_obama[i][1]
    # Tuples are immutable: can't edit a part of it, 
    # need to recreate the whole thing and then assign it
    sorted_by_date_obama[i] = (sorted_by_date_obama[i][0], obama_to_date)
xs_obama,ys_obama = zip(*sorted_by_date_obama) # zip(*x) unzips list x

sorted_by_date_mccain = sorted(mccaindonations.items(), key=lambda (key,val): key)
mccain_to_date = 0
for i in range( len(sorted_by_date_mccain) ):
    mccain_to_date += sorted_by_date_mccain[i][1]
    # Same as above
    sorted_by_date_mccain[i] = (sorted_by_date_mccain[i][0], mccain_to_date)
xs_mccain,ys_mccain = zip(*sorted_by_date_mccain)

# matplotlib places the two seprate x-value lists on the same x-axis.
# Note that len(xs_?) must equal len(ys_?)
plt.plot(xs_obama, ys_obama, label='Obama\'s Donations')
plt.plot(xs_mccain, ys_mccain, label='McCain\'s Donations')
plt.legend(loc='upper center', ncol = 4)
plt.savefig('test_obama_mccain.png', format='png')