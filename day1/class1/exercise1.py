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


# dictionaries 
sorted_by_date_obama = sorted(obamadonations.items(), key=lambda (key,val): key)
xs_obama,ys_obama = zip(*sorted_by_date_obama) # zip(*x) unzips list x

sorted_by_date_mccain = sorted(mccaindonations.items(), key=lambda (key,val): key)
xs_mccain,ys_mccain = zip(*sorted_by_date_mccain)

# matplotlib places the two seprate x-value lists on the same x-axis.
# Note that len(xs_?) must equal len(ys_?)
plt.plot(xs_obama, ys_obama, label='Obama\'s Donations')
plt.plot(xs_mccain, ys_mccain, label='McCain\'s Donations')
plt.legend(loc='upper center', ncol = 4)
plt.savefig('test_obama_mccain.png', format='png')