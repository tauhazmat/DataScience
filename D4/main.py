print("This Directory contains Data Visualization Files")



# How to make a simple barplot (practice)
import seaborn as sns
import matplotlib.pyplot as plt

titaic_dataset = sns.load_dataset("titanic")
titanic

plt.barplot(x= "sex", y="fare", data=titanic)
# plt.show()  commented out plt.show so preview is not shown
