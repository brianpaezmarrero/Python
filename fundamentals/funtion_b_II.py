#create a funtion
#it can acept a number
# def count_down(a):
#     output = []
#     for x in range(a,-1,-1):
#         output.append(x)
#     return output
# #make the number return to a list like a countdown
# print(f"Countdown: {count_down(5)}")

# Print and Return 
# -Create a function that will receive a list with two numbers.
# Print the first value and return the second.
# def print_recieve(a):
#     print(a[0])
#     return a[1]
# print(print_recieve([1,2]))
# Example: print_and_return([1,2]) should print 1 and return 2


# First Plus Length 
# -Create a function that accepts a list and returns the sum of the 
#             first value in the list plus the list's length.
# def first_plus_length(add):
#     return add[0] + len(add)
# print(first_plus_length([1,2,3,4,5]))
# Example: first_plus_length([1,2,3,4,5])
# should return 6 (first value: 1 + length: 5)


# Values Greater than Second 
#-Write a function that accepts a list and creates a new list containing
#only the values from the original list that are greater than its 2nd value.
#Print how many values this is and then return the new list.
#If the list has less than 2 elements, have the function return False
# def values_greater_than(list):
#     if len(list) < 2:
#         return False
#     output = []
#     for i in range(0,len(list)):
#         if list[i] > list[1]:
#             output.append(list[i])
#     print(len(output))
#     return output

# print(values_greater_than([5,2,3,2,1,4]))
# print(values_greater_than([3]))

# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

# This Length, That Value 
#-Write a function that accepts two integers as parameters: size and value.
#The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def lenth_and_value(size, value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(lenth_and_value(4,7))
print(lenth_and_value(6,2))
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]