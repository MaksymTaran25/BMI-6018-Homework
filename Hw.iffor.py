# Logical Processing Homework

# Problem 1 Stacking logical operators

influenza_genome = [19, 15, 7, 9, 12, 6, 17, 20, 29, 14, 22, 8, 15, 12, 21, 25, 11, 10, 30, 4, 6, 24, 18, 21, 28, 22, 13, 19, 4, 23, 16, 25, 13, 28, 16, 29, 4, 3, 25, 13, 10, 26, 26, 18, 25, 28, 24, 18, 3, 9, 11, 29, 30, 16, 24, 5, 5, 25, 14, 7, 1, 15, 6, 6, 19, 19, 15, 2, 14, 7, 21, 5, 26, 25, 18, 18, 9, 7, 27, 4, 1, 23, 30, 25, 24, 29, 11, 16, 20, 15, 2, 9, 8, 13, 1, 13, 5, 17, 29, 25, 16, 13, 3, 30, 10, 21, 9, 18, 20, 14, 20, 19, 6, 4, 20, 5, 14, 5, 12, 27, 18, 28, 13, 30, 6, 9, 12, 9, 29, 4, 14, 22, 7, 25, 11, 12, 5, 24, 6, 3, 8, 3, 20, 24, 8, 23, 22, 11, 22, 10, 13, 14, 2, 6, 22, 22, 7, 6, 18, 28, 25, 4, 6, 24, 10, 24, 15, 18, 12, 24, 10, 16, 24, 21, 19, 24, 8, 8, 8, 10, 8, 15, 26, 14, 21, 18, 6, 10, 23, 2, 20, 15, 1, 4, 20, 8, 6, 1, 4, 15, 21, 26, 25, 1, 24, 15, 27, 8, 23, 4, 30, 22, 1, 3, 7, 16, 18, 29, 11, 4, 1, 29, 30, 16, 30, 10, 2, 26, 26, 7, 10, 15, 6, 25, 4, 7, 12, 24, 5, 8, 23, 16, 8, 3, 16, 1, 9, 4, 27, 26, 9, 25, 7, 14, 27, 21, 27, 28, 2, 2, 27, 22, 3, 23, 14, 16, 30, 12, 14, 8, 10, 5, 16, 12, 24, 3, 28, 9, 21, 7, 25, 9, 5, 3, 27, 7, 29, 25, 13, 11, 25, 21, 2, 14, 8, 17, 18, 23, 22, 12, 7, 26, 11, 25, 1, 23, 9, 12, 2, 4, 17, 27, 9, 13, 19, 15, 10, 12, 21, 25, 5, 1, 16, 17, 28, 23, 18, 10, 15, 18, 1, 11, 14, 10, 18, 12, 1, 23, 23, 25, 13, 27, 27, 6, 9, 11, 23, 6, 23, 14, 9, 15, 11, 24, 11, 29, 18, 6, 19, 16, 14, 26, 2, 14, 15, 25, 6, 21, 23, 25, 27, 5, 1, 17, 4, 7, 18, 8, 9, 10, 5, 21, 29, 9, 6, 2, 22, 12, 1, 13, 19, 6, 17, 21, 22, 26, 21, 10, 29, 8, 13, 10, 29, 6, 29, 16, 30, 5, 25, 14, 15, 15, 9, 24, 13, 5, 28, 18, 11, 21, 15, 12, 5, 16, 5, 29, 29, 29, 3, 10, 24, 16, 16, 12, 14, 6, 22, 21, 10, 10, 2, 14, 9, 29, 29, 2, 26, 11, 6, 7, 28, 10, 3, 24, 30, 2, 23, 9, 29, 27, 19, 1, 15, 11, 5, 7, 9, 26, 28, 27, 10, 20, 23, 29, 10, 15, 30, 13, 2, 11, 5, 9, 2, 30, 27, 14, 11, 20, 19, 1, 12, 10, 8, 6, 16, 3, 25, 5, 10, 24]
influenza_genome_copy = influenza_genome.copy() # created copy of unmodified list to modify it again in exercise 4
# Given the array influenza_genome, write code that uses for loops and if statements to do the following and print the results(see below for instructions):

# 1.1 add 1 to the value at the index 300.
for i in range(300, 301): # for element with index 300
    influenza_genome[i] +=1 # added 1 to element with index 300
print("The answer for 1.1 is", influenza_genome[300], "at the index 300")
print() # I made this line just to separate prints for answers in console
# 1.2 for the first 30 elements, if the value of the element is divisable by 3, multiply the value by 3.
for i in range(30): # for the first 30 elements
    if influenza_genome[i] % 3 == 0: # if element is divisible by 3
        influenza_genome[i] *= 3 #multiplying value of element by 3
        print("The answer for 1.2 is", influenza_genome[i], "at the index", i)
print()
# 1.3 for the last 30 elements, if the index value at that point is divisable by 5, replace the value with "a".
array_lenght = len(influenza_genome) # creating variable which equals the length of array
for i in range (array_lenght - 30, array_lenght): # for last 30 elements in array
    if i % 5 == 0: # if index is divisible by 5
        influenza_genome[i] = "a" # changing value of element for "a"
        print("The answer for 1.3 is", influenza_genome[i], "at the index", i)
print()
# 1.4 for all elements between index 200 and 300, if the value of the element is divisable by BOTH 3 AND 5, replace the value with the 10.
for i in range(200, 301): # for elements with index between 200 and 300
    if influenza_genome[i] % 3 == 0 and influenza_genome[i] % 5 == 0: #if the value of the element is divisable by both 3 AND 5
        influenza_genome[i] = 10 # changing value of element for 10
        print("The answer for 1.4 is", influenza_genome[i], "at the index", i)
print()
# Only print the section of the array that is modified after completing each operation. i.e only print index 300 of the array after 1.1 and only the first 30 elements after 1.2



# Problem 2 Loops within loops
# Given the array influenza_genome, write code using both for and while loops that:

# 2.1 Create a for loop that iterates over items index 234 through 237 and prints each value (ie there should be 4 items)
for i in range(234, 238): # for elements with index 234,235,236,237
    print("The answer for 2.1 is", influenza_genome[i], "at the index", i)
print()
# 2.2 Create a while loop that iterates over items index 234 through 237 and prints each value (ie there should be 4 items)
i = 234 # creating variable with starting value 234 for while lopp condition
while 234 <= i <= 237: # while elements have index 234,235,236,237
    print("The answer for 2.2 is", influenza_genome[i], "at the index", i)
    i += 1 # adding 1 each iteration
print()
# 2.3 Create a for loop that iterates over items index 234 through 237 and if the index is 236 print the item 7 times.
for i in range(234, 238): # for elements with index 234,235,236,237
    if i == 236: # if index equals 236
        for a in range(7): # for loop to repeat 7 times
            print("The answer for 2.3 is", influenza_genome[i], "at the index", i)
    else:
        print("The answer for 2.3 is", influenza_genome[i], "at the index", i)
print()



# Problem 3 Functions
# You are going to implement 3 funtions that will process the influenza_genome list in various ways.

# 3.1 write a function, that takes in the array as an argument, and outputs 10 values from the dataset, spaced out by indexes that are 25 apart (ie 0, 25, 50, etc)
def function1(array): # defining function "function1"
    for i in range(0, len(array), 25): # range from 0 to last index of function with increment value 25
        print("The answer for 3.1 is", influenza_genome[i], "at the index", i)
function1(influenza_genome) # calling fucntion1
print()
# 3.2 write a function that takes in the dataset as an argument and outputs 20 values from the dataset, spaced out by indexes that are y apart (ie you can decide how far apart they should be iterated as long as they dont exceed the length of the dataset)
def function2(dataset, y): # defining function "function1" which accepts dataset and increment value as an arguments
    amount = 0 # defining variable to count iterations
    output_list = [] # created list to store every line from output
    for i in range(0, len(dataset), y): # for elements with index from 0 to length of dataset with increment value y
        amount += 1 # adding 1 each iteration
        if amount == 20:# if its 20th iteration stop iterating
            break
        else:
            output = "The answer for 3.2 is", dataset[i], "at the index", i # created variable "output" to story output from each iteration
            output_list.append(output) # added every output to list to make my next function "function3 work better
    return output_list #returned list with every output line
print(function2(influenza_genome,20)) # calling fucntion2
print()
# 3.3 write a function that takes the output from the function from 3.2 as an argument, then only prints out every other item (ie there should only be 10 outputs)
def function3(output): #defining function which accepts output / I am not sure in which type you wanted output of the function to be accepted so I decided to completely change previous function and create a list in there which will store it 
    for i in range(0, len(output), 2): # iterates through every second item in my list
        print(output[i])

function3(function2(influenza_genome,20)) #calling function3
print()
# Problem 4 Putting it all together
# Write a function that implements the code from problem 1.4, then implements the code from problem 2.3.

# The function should create a modified version of the influenza_genome list as per 1.4, then print the section described in problem 2.3. 
def function4(array): # my function takes the copy of the original list and then modifies it as per 1.4
    for i in range(200, 301): # for elements with index between 200 and 300
        if array[i] % 3 == 0 and array[i] % 5 == 0: #if the value of the element is divisable by both 3 AND 5
            array[i] = 10 # changing value of element for 10
    for i in range(234, 238): # for elements with index 234,235,236,237
        if i == 236: # if index equals 236
            for a in range(7): # for loop to repeat 7 times
                print("The answer for 4.1 is", array[i], "at the index", i)
        else:
            print("The answer for 4.1 is", array[i], "at the index", i)

function4(influenza_genome_copy) # called function and putted copy of original list as an argument / I created it on line 6
