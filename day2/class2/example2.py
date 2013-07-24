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

plt.savefig('day2.png', format='png')