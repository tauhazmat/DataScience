# For Practice
import seaborn as sbn
import matplotlib.pyplot as plt

# Import Data Set
flower_data = sbn.load_dataset("iris")
flower_data

plt.barplot(x = "petal_length", y = "petal_width", data = flower_data)
plt.show()










# Titanic dataset
import seaborn as sns
import matplotlib.pyplot as plt

titaic_dataset = sns.load_dataset("titanic")
titanic

plt.barplot(x= "sex", y="fare", data=titanic)
plt.show() # Preview shown
