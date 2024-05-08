import matplotlib.pyplot as plt
import numpy as np

def plot_data(file_obj):
	# Read data from the file object
	data = np.genfromtxt(file_obj, delimiter=' ')

	# Split data into x and y values
	x_values = data[:, 0]
	y_values = data[:, 1]

	# Create the scatter plot
	plt.scatter(x_values, y_values)
	plt.xlabel('X Axis')
	plt.ylabel('Y Axis')
	plt.title('Scatter Plot of Data')
	plt.show()
with open('x_y_coordinates.txt', 'r') as file_obj:
     plot_data(file_obj)
