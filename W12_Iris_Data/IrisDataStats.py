'''
https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
Loads a dataset with assosciated attribute names, then reports on details
of the dataset including statistics and graphs
'''

# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt


# Load dataset
file = "iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
#load data from csv file with columns labeled by names into dataframe called dataset
dataset = pandas.read_csv(file, names=names)

# shape
print("The file "+file+" has data with dimensions: ")
print(dataset.shape)

# head
print("The first 20 data points are: ")
print(dataset.head(20))

# descriptions
print("The descriptive statistics for each column of the data are: ")
print(dataset.describe())

# class distribution
print("The type and number of each iris: ")
print(dataset.groupby('class').size())

# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(
    2, 2), sharex=False, sharey=False)
plt.savefig('box.png')
print("Boxplot created in the same directory as this script")

# histograms
dataset.hist()
plt.savefig('hist.png')
print("Histogram created in the same directory as this script")

# scatter plot matrix
scatter_matrix(dataset)
plt.savefig('matrix.png')
print("Scatterplot created in the same directory as this script")
