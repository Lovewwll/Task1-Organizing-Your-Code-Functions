# Press Shift+F10 to execute it or replace it with your code.



import matplotlib.pyplot as plt

# Sample data
points = [
    [-18.9686, 31.1668],  # Point 1
    [-17.8274, 31.0521],  # Point 2
    [-20.1505, 28.5845],  # Point 3
    [-19.8327, 32.7649],  # Point 4
    [-17.5222, 30.9737],  # Point 5
    [-18.3712, 26.4995],  # Point 6
    [-20.2901, 30.0582],  # Point 7
    [-16.5174, 28.7902],  # Point 8
    [-19.3458, 29.5485],  # Point 9
    [-17.9009, 25.8201],  # Point 10
    [-20.2739, 29.4214],  # Point 11
    [-18.9622, 31.0444],  # Point 12
    [-16.5261, 30.8099],  # Point 13
    [-19.3597, 30.8711],  # Point 14
    [-17.8136, 29.4608],  # Point 15
    [-19.7907, 31.0036],  # Point 16
    [-18.3141, 27.0326],  # Point 17
    [-19.4346, 29.8174],  # Point 18
    [-20.2277, 29.1534],  # Point 19
    [-17.3569, 30.1662],  # Point 20

]

x = [point[0] for point in points]  # x coordinates
y = [point[1] for point in points]  # y coordinates
point_numbers = range(1, len(points) + 1)  # Point numbers

# Create the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, c='orange', alpha=0.7, label='Traverse data')

# Add point numbers as annotations
for i, (xi, yi, point_number) in enumerate(zip(x, y, point_numbers)):
    plt.annotate(point_number, (xi, yi), textcoords="offset points", xytext=(0, 10),fontsize=8)

# Label axes and add a title
plt.xlabel('x')
plt.ylabel('y')
plt.title('TRAVERSE VISUALISATION')
plt.grid(False)

# Add legend
plt.legend()

plt.show()
