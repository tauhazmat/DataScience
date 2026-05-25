# while loops and for loops


# While loops
# x = 0
# while (x <= 5):
#     print(x)
#     x = x + 1



# For loops
# for x in range (5,10):
#     print(x)
 

# array
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for d in days:
    # if (d=="Thu"):break # stops when thursay comes
    if (d== "Fri"):continue #skips when d comes on friday
    print(d)