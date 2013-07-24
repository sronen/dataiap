import numpy
import welchttest

town1_heights = [5, 6, 7, 6, 7.1, 6, 4]
town2_heights = [5.5, 6.5, 7, 6, 7.1, 6]

print "Welch's T-Test p-value:", welchttest.ttest(town1_heights, town2_heights)