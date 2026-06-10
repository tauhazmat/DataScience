# For Practice
import seaborn as sbn
import matplotlib.pyplot as plt

# Import Data Set
flower_data = sbn.load_dataset("iris")
flower_data

plt.barplot(x = "petal_length", y = "petal_width", data = flower_data)
plt.show
