# Logical operators are either  "true or false"    or    "yes or no"   or    "1 or 0"
# equal to                  ==
# less than                 <
# greater than              >
# less than equal to        <=
# greater than equal to     >=


# is 4 equal to 4?
# print(4 == 4) # true
# print(4 != 4) # false
# print(4 > 3) # true
# print(3 > 6) # false
# print(3 <= 5) # true
# print(5 >= 4) # true


# Application of logical operators
# Q) Alex is 4 years old. He needs to go to school but the age required to join school is 5 y/o. Can Alex go to school?
# alex_age = 4
# age_requirement_for_school = 5
# print(alex_age >= age_requirement_for_school)


# input operator and logicals
age_requirement_for_school = 5
child_age = input("Enter child age: ") # input function
child_age = int(child_age)
print(type(child_age)) 
print(child_age == age_requirement_for_school) #logical operator

