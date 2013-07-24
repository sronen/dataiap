import matplotlib.pyplot as plt
import random
random.seed(0)

fig = plt.figure(figsize=(50, 30))

# data
N = 100
xs = range(N)
ys1 = [random.randint(0, 50) for i in xs]
ys2 = range(N)

# matplotlib automatically scales the x and y axes, so the sizes of the bars depend on their relative values

#
# bar
#
# Possible customizations:
#color='blue': set color to a hex value ("#ffffff"), a common color name ("green"), or a shade of grey ("0.8").
#linewidth=1: the width of the bar's border. set it to 0 to remove the border.
#edgecolor='blue': set the color of the bar's border.
#label='a name': give a set of bars a name. Later, we will teach you how to create legends that will display the labels.
#
import numpy as np
left = np.arange(len(xs)) # return evenly-spaced values between 0 and len(xs) within an interval of 1
offset = 0
width = 0.25

subplot = fig.add_subplot(3,2,1)
subplot.bar(left, ys1, width=width)
subplot.bar(left+offset, ys2, width=width, bottom=ys1, color='red') # places another set of bars on top of the first one.

#
# plot
#
# Possible customizations:
#color='green': same as color for bar graphs
#marker=None: specify the marker to draw at each point. I commonly use '*', '+', '.' or 'o'. Set it to None to not draw markers. The documentation has a full list of the available markers.
#label='a name': give a line a name. I usually call plot() for each line if I want to give each one a name.
#
subplot = fig.add_subplot(322)
#subplot.plot(xs, ys1, xs, ys2) # shorthand for plot(xs, ys1) followed by plot(xs, ys2). The latter draws a straight line.
subplot.plot(xs, ys1, marker='*') # use full notation to add keywords, e.g., 'marker'
subplot.plot(xs, ys2) 

# 
# boxplot
#
# Possible customizations:
#vert=1: By default, the boxes are drawn vertically. You can draw them horizontally by setting vert=0
#widths=None: Like width in bar charts, this sets the width of each box
#
subplot = fig.add_subplot(323)
boxdata1 = [random.randint(0, 20) for i in xrange(10)]
boxdata2 = [random.randint(20,40) for i in xrange(10)]
boxdata3 = [random.randint(40,60) for i in xrange(10)]
data = [boxdata1, boxdata2, boxdata3]
subplot.boxplot(data)

#
# scatterplot
#
# Possible customizations:
#s=20: sets the size of each point to 20 pixels.
#c='blue': sets the color of each point to blue
#marker='o': each point will be drawn as a circle. The documentation lists large number of other markers
#alpha=None: the alpha (transparency) value of the points. Between 0 and 1.
#linewidth=4: sets the width of the line around the point to 4 pixels. I usually set it to 0.
#
#
subplot = fig.add_subplot(324)
subplot.scatter([0, 1, 2], [9, 3, 10]) # pass an x,y pair OR a list of x and a list of y values

#
# choropleths/maps
#

relbasepath = "../../dataiap/" # base path relative to the directory of the program

import sys
# this adds the resources/util/ folder into your python path
# you may need to edit this so that the path is correct
sys.path.append(relbasepath + 'resources/util/')
from map_util import *

import json

# Map of Counties
#
subplot = fig.add_subplot(325)
# data is a list of strings that contain fips values
data = json.load(file(relbasepath + 'datasets/geo/id-counties.json'))
for fips in data:
    draw_county(subplot, fips)

# Map of States
#
subplot = fig.add_subplot(326)
data = json.load(file(relbasepath + 'datasets/geo/id-states.json'))
for state in data:
    draw_state(subplot, state)

plt.savefig('day2.png', format='png')