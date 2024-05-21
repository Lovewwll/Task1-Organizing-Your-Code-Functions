import pandas as pd
import matplotlib.pyplot as plt


def plot_data(file):
    """
    Plots a scatter plot from a file object.

    Parameters:
    file (file object): A file object containing the data.

    Returns:
    None
    """
    # Read the data into a DataFrame
    data = pd.read_csv(file)

    # Check if the DataFrame has at least two columns
    if data.shape[1] < 2:
        raise ValueError("The data should have at least two columns for a scatter plot")

    # Extract the first two columns for the scatter plot
    x = data.iloc[:, 0]
    y = data.iloc[:, 1]

    # Create the scatter plot
    plt.scatter(x, y)

    # Label the axes
    plt.xlabel(data.columns[0])
    plt.ylabel(data.columns[1])

    # Set a title
    plt.title('Scatter Plot')

    # Display the plot
    plt.show()


# Example usage:
# file named 'data.csv' with appropriate data
with open('data.csv', 'r') as file:
    plot_data(file)
