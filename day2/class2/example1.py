import matplotlib.pyplot as plt
import random
random.seed(0)

fig = plt.figure(figsize=(50, 30))

N = 100
xs = range(N)
ys = [random.randint(0, 50) for i in xs]
ys2 = range(N)

# matplotlib automatically scales the x and y axes, so the sizes of the bars depend on their relative values

import numpy as np
left = np.arange(len(xs)) # return evenly-spaced values between 0 and len(xs) within an interval of 1
width = 0.25

'''
*Possible customizations:
color='blue': set color to a hex value ("#ffffff"), a common color name ("green"), or a shade of grey ("0.8").
linewidth=1: the width of the bar's border. set it to 0 to remove the border.
edgecolor='blue': set the color of the bar's border.
label='a name': give a set of bars a name. Later, we will teach you how to create legends that will display the labels.
'''

subplot = fig.add_subplot(3,2,1)
subplot.bar(left, ys, width=width)
subplot.bar(left+width, ys2, width=width, bottom=ys, color='red') # places another set of bars on top of the first one.

#raw_input('Press a key')
plt.savefig('day2.png', format='png')