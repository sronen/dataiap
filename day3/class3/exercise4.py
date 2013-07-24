import csv,sys
import welchttest

reader = csv.DictReader( open(sys.argv[1], 'r') )

obama_don = []
mccain_don = []

for row in reader:
	name = row['cand_nm']
	amount = float(row['contb_receipt_amt']) # need a number, not string! Otherwise boxplot wouldn't run!
	
	if 'Obama' in name:
		obama_don.append(float(amount))
	elif 'McCain' in name:
		mccain_don.append(float(amount))

print "Welch's T-Test p-value:", welchttest.ttest(obama_don, mccain_don)