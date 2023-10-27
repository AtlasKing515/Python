import numpy as np

x0 = float(input("Enter x0: "))
s = float(input("Enter s: "))
x_start = float(input("Enter the initial value of x interval: "))
x_end = float(input("Enter the final value of x interval: "))
n = int(input("Enter the number of points in the table: "))

x_values = np.linspace(x_start, x_end, n)

y_values = np.exp(-((x_values - x0) ** 2) / (2 * s ** 2)) / (s * np.sqrt(2 * np.pi))

print("x\t\ty")
for x, y in zip(x_values, y_values):
    print("{:.3f}\t\t{:.5f}".format(x, y))
