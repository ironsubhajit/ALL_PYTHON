import matplotlib.pyplot as plt

values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(values, squares, linewidth=5)

# chart title label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Value", fontsize=14)

#  Set tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()