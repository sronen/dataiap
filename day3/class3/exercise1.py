import csv,sys
import numpy as np

reader = csv.DictReader( open(sys.argv[1], 'r') )

obama_don = []
mccain_don = []

for row in reader:
	name = row['cand_nm']
	amount = float(row['contb_receipt_amt']) # need a number, not string
	
	if 'Obama' in name:
		obama_don.append(amount)
	elif 'McCain' in name:
		mccain_don.append(amount)

# not working! Maybe i should calculate on my own...
obama_mean = np.mean(obama_don)
mccain_mean = np.mean(mccain_don)

print "Obama avg. donation", obama_mean
print "McCain avg. donation", mccain_mean

print "Effect size: ", abs(obama_mean - mccain_mean)