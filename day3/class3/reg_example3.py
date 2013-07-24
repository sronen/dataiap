import matplotlib.pyplot as plt

timings = range(1, 100)
displacements = [4.9*t*t for t in timings]

sq_timings = [t*t for t in timings]

fig = plt.figure()
subplot = fig.add_subplot(211)
subplot.scatter(timings, displacements, color="#1f77b4")
subplot.set_title("original measurements (parabola)")

subplot = fig.add_subplot(212)
subplot.scatter(sq_timings, displacements, color="#1f77b4")
subplot.set_title("squared time measurements (line)")

plt.savefig('parabola-linearized.png', format='png')