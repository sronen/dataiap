import matplotlib.pyplot as plt
from collections import Counter

town1_heights = [5, 6, 7, 6, 7.1, 6, 4]
town2_heights = [5.5, 6.5, 7, 6, 7.1, 6]
'''
increment = 1
width= .25

# map(f, list) runs f on each item of list
# lambda ammt means for item 'ammt' return ammt - ammt%increment, which is a smart way of flooring: ammt%increment returns the remainder of division by 1 (=the non-integer part), which is then subtracted from the original ammt, leaving us with the integer part
town1_bucketted = map(lambda ammt: ammt - ammt%increment, town1_heights)
town2_bucketted = map(lambda ammt: ammt - ammt%increment + width, town2_heights)
town1_hist = Counter(town1_bucketted) # A dictionary that counts the number of appearances for each key; in our case, for each floored height.
town2_hist = Counter(town2_bucketted)

minamount = min(min(town1_heights), min(town2_heights))
maxamount = max(max(town1_heights), max(town2_heights))
buckets = range(int(minamount), int(maxamount)+1, increment)
'''
fig = plt.figure()
sub = fig.add_subplot(111)
sub.boxplot([town1_heights, town2_heights], whis=1)
sub.set_xticklabels(("Town 1", "Town 2"))
sub.set_title("Town 1 vs. Town 2 Heights")
plt.savefig('town_boxplots.png', format='png')