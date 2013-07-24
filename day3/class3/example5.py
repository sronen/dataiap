import numpy
import welchttest

town1_heights = [5, 6, 7, 6, 7.1, 6, 4]
town2_heights = [5.5, 6.5, 7, 6, 7.1, 6]

print "Welch's T-Test p-value:", welchttest.ttest(town1_heights, town2_heights)

import scipy.stats

print "Town 1 Shapiro-Wilks p-value", scipy.stats.shapiro(town1_heights)[1]

print "Mann-Whitney U p-value", scipy.stats.mannwhitneyu(town1_heights, town2_heights)[1]