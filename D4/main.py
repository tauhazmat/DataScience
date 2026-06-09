print("This Directory contains Data Visualization Files")  # D4/Data-Visualization
print(titanic_dataset)
print(car_crashes)



# How to make a simple barplot (practice)
import seaborn as sns
import matplotlib.pyplot as plt

titaic_dataset = sns.load_dataset("titanic")
titanic

plt.barplot(x= "sex", y="fare", data=titanic)
# plt.show()  commented out plt.show so preview is not shown



# making a data set of IRIS
import seaborn as sns
import matplotlib.pyplot as plt

flower = sns.load_dataset("iris")
flower # Shows a chart of data of the flower "Iris"

plt.barplot(x= "petal_width", y="petal_length", data=flower)
# plt.show()  commented out plt.show() 


# making data set of tips
import seaborn as sns
import matplotlib.pyplot as plt

tipsdata = sns.load_dataset("tip")
tip # Shows a chart of data of the flower "Iris"

plt.barplot(x= "petal_width", y="petal_length", data=tipsdata)
# plt.show()  commented out plt.show() 

def printalldata():
  print(titaic_dataset)
  print(flower)
  print(tipsdata)

printalldata()   # Prints all data




car_data = sns.load_dataset("carcrashes") #data for cars-
