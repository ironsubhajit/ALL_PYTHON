import matplotlib.pyplot as plt


x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
#plt.tick_params(axis='both', which='major', labelsize=14)
y_max = (5200 ** 3)
#  set the range for each axis
plt.axis(xmin=0, xmax=5300, ymin=0, ymax=y_max)

plt.show()
#plt.savefig('squares_plot.png', bbox_inches='tight')