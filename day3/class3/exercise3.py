import csv,sys
import matplotlib.pyplot as plt

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

fig = plt.figure()
sub = fig.add_subplot(111)
sub.boxplot([obama_don, mccain_don], whis=1)
sub.set_xticklabels(("Obama", "McCain"))
sub.set_title("Obama vs. McCain Donations")
sub.set_ylim((-250, 1250)) # limit y axis to this range -- make it easier to read
plt.savefig('donations_boxplots.png', format='png')