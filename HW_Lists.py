"""BMI 6018 Fall 2022 

Instructions: For this assignment, please return all answers as variables in your
.py file. You will quickly note that you will need to find answers outside the
class lectures. This is not an accident! You will need to become professionally
comfortable with looking things up via the python docs and google. 

Ensure that all variables are labelled according to the example. IE the answer
to problem 1 part c should be labelled one_c. While all questions are answerable
with a single line of code, you are free to use helper variables so long as they
are helpfully/informatively named. 

I should be able to open your .py file and run it without errors. I will **not** be 
debugging your code for you. If your file does not run, it will **not** be graded. 
If you are unsure if your file will run, open up a chpc terminal and test it there.

For this assignment, please only use base python files types. That is: there 
should be no import calls in your file save my use of sys at the end.

Example Problem

0.a Create a list of strings
0.b Using a str method, capitalize one of the elements in the list using a slice
0.c Coerce one character of the list to display as a hex

zero_a = ['first','second','third','fourth','fifth']
zero_b = zero_a[1].upper()
zero_c = hex(ord(zero_a[1][1]))

#Problem 1: Lists, Sets and Coersion

1.a Create a list of integers no fewer than 10 items from 0 to 9.
 .b Add 3 to the 5th indexed element
 .c Coerce all elements in the list to floats using list comprehension
 .d Coerce the list to a set
 .e Using a method, append int 10 to the set
 .f Using a method, pop an item from the set
 .g Using a length counting function, count the number of items in the set
 .h Check if the number of items in the set is the same as the 
    number of items in the list
 .i Coerce the set to a list and use the "+" operator combine the list to the list from 1.a
 .j Coerce 1.i to a set
 .k Count the number of elements in the 1.j



Problem 2: Dictionary woes

2.a Combine the three sample dictionaries (given below) into a nested dictionary (nested in programming means joined), named 
    two_a, ensure the key names are the same as the dictionary names.
 .b Using keys, retrieve the Dango's name from 2.a
 .c Using keys, update the value of Mochi's year to 2018. This should not be a variable
    and should simply update 2.a.
 .d Manually create a dictionary that has a single level and contains each patient
    as the key and the year as the value. Set Mochi's year to 2019.'
 .e Coerce the keys of 2.d into a list
 .f Coerce the values of 2.d into a list
 .g Use the zip function to combine 2.e and 2.f into a dictionary again


two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}



Problem 3: Set combinations

Given the predefined sets below and using set methods
3.a Is set E a subset of set A
 .b Is set E a strict subset of set A
 .c Create a set that is the intersection of set A and set B
 .d Create a set that is the union of sets C, D and E
 .e add 9 to the set
 .f Using == compare this set to the list in one_a
 .g Explain why they are not the same. What would you need to change if you
    wanted this to be True?
 

three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}



Problem 4: Changing variable types

For each step you will modify a variable, then append the type of the variable
to a list. Do not recreate the list variable, it should be a running list of 
types.

4.a Create a variable of type int with the value of 8
 .b Create an empty list 
 .c Using type(), add the type of 4.a to this list
 .d Add 0.39 to 4.c
 .e append the type of 0.39 to the list
 .f exponentiate to the -10, ie: 4.d^-10,(hint: there might be an artihmetic operator to do so) round it to no 
    decimal places, and append to list.
 .g append the type to the list
 
 
Problem 5: More variable type changes

Continue from where you left off in Problem 4.

5.a Manually create a dictionary where the values are items in the list from where we left in 
    problem 4, and the keys should be their index in the list. Print the dictionary.
 .b Add 300 and coerce it into a string
 .c append the type to the list
 .d slice the string up to the 2nd element
 .e append the type to the list
 .f use list comprehension to convert this into a new list of integers
 .g append the type to the list
 .h append the type of three_setA to the list
"""

#Start your assignment here
print("Assignment 1") 

one_a = [0 , 1, 2, 3, 4, 5, 6, 7, 8, 9] # created list to perfrom different methods on it
print("The answer to 1.a is: ", one_a)

one_b = list(one_a) # assigned values of list one_a to one_b
one_b[5] += 3 # added 3 to the elevement with index 5 of list one_b
print("The answer to 1.b is: ", one_b)

one_c = [float(i) for i in one_a ] #coerced all elements of list one_b to float and assignes it to list one_c
print("The answer to 1.c is: ", one_c)

one_d = set(one_a) # created set one_d from list to perfrom different methods on it
print("The answer to 1.d is: ", one_d)

one_e = set(one_d)  # assigned values of list one_d to one_e
one_e.add(10) # appended 10 to the list one_e
print("The answer to 1.e is: ", one_e)

one_f = one_d.pop() #poped item from list one_f
print("The answer to 1.f is: ", one_f)

one_g = len(one_d) # found the length of list one_d
print("The answer to 1.g is: ", one_g)

if len(one_a) == len(one_d): # in case length of both lists are equal print that
    one_h = f"The answer to 1.h is: Yes, the length of both is {len(one_a)}" 
else: #in other case print that they are not equal
    one_h = f"The answer to 1.h is: No, the length of list is {len(one_a)} and the length of set is {len(one_d)}"
print(one_h)

one_i = list(one_d) + one_a # coerced set one_d to list and combined with list one_a
print("The answer to 1.i is: ", one_i)

one_j = set(one_i) # coerced list one_i to set one_j
print("The answer to 1.j is: ", one_j)

one_k = len(one_j) # assigned amount of elements one_j to one_k
print("The answer to 1.k is: ", one_k)


print("Assignment 2") 

two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}

two_a = {
    "two_patient_dictionary_kinoko" : two_patient_dictionary_kinoko,
    "two_patient_dictionary_dango" : two_patient_dictionary_dango,
    "two_patient_dictionary_mochi" : two_patient_dictionary_mochi,
}
print("The answer to 2.a is: ", two_a)

two_b = two_a["two_patient_dictionary_dango"]["name"]
print("The answer to 2.b is: ", two_b)

two_a["two_patient_dictionary_mochi"]["year"] = 2018
print("The answer to 2.c is: ", two_a)

two_d = {
    two_patient_dictionary_kinoko["name"] : two_patient_dictionary_kinoko["year"],
    two_patient_dictionary_dango["name"] : two_patient_dictionary_dango["year"],
    two_patient_dictionary_mochi["name"] : two_patient_dictionary_mochi["year"]
}
two_d["Mochi"] = 2019 # setted Mochi's year to 2019
print("The answer to 2.d is: ", two_d)

two_e = list(two_d.keys()) #coerced keys of 2.d into a list two_e
print("The answer to 2.e is: ", two_e)

two_f = list(two_d.values()) #coerced values of 2.d into a list two_e
print("The answer to 2.f is: ", two_f)

two_g = {two_e: two_f for two_e, two_f in zip(two_e, two_f)} #zipped combination of 2.e and 2.f into dictionary 
print("The answer to 2.g is: ", two_g)

print("Assignment 3")

three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}

three_a = three_setE.issubset(three_setA) #checks uf set e us a subset of set a
print("The answer to 3.a is: ", three_a)

three_b = three_setE < three_setA # checks if e is a strict subset of set a
print("The answer to 3.b is: ", three_b)

three_c = three_setA.intersection(three_setB)
print("The answer to 3.c is: ", three_c)

three_d = three_setC.union(three_setD,three_setE)
print("The answer to 3.d is: ", three_d)

three_d.add(9)
three_e = three_d
print("The answer to 3.e is: ", three_e)

if three_e == one_a:
    three_f = "Equal"
else:
    three_f = "Not equal"
print("The answer to 3.f is: ",three_f)

three_g = "Firsly, we will need to remove 0 from one_a, secondly we will need coerce one_a to a set"
print("The answer to 3.g is: ", three_g)

print("Assignment 4")
four_a = 8
print("The answer to 4.a is: ", four_a)

four_b = []
print("The answer to 4.b is: ", four_b)


four_b.append(type(four_a))
print("The answer to 4.c is: ", four_b)

four_b.append(0.39) # appended 0.39 to list four_b
print("The answer to 4.d is: ", four_b)

four_b.append(type(0.39)) 
print("The answer to 4.e is: ", four_b)


four_f = round(0.39**10, 0) # rounded 0.39 ** 10 to no decimal which equal 0.0
four_b.append(four_f) 
print("The answer to 4.f is: ", four_b)

four_b.append(type(four_f)) 
print("The answer to 4.g is: ", four_b)


print("Assignment 5")


five_a = { #manually created list where values are items and keys are there index
    "0" : four_b[0],
    "1" : four_b[1],
    "2" : four_b[2],
    "3" : four_b[3],
    "4" : four_b[4]
}
print("The answer to 5.a is: ", five_a)

four_b.append(str(300)) # I am not sure where I need to add 300 because its not said in the task, so I appended it to four_b
print("The answer to 5.b is: ", four_b)

four_b.append(type(four_b[5])) # I am not sure where I need to add type of 300 because its not said in the task, so I appended it to four_b
print("The answer to 5.c is: ", four_b)

slice_string = four_b[5] #getting "300" from list in order to slice it
slice_string = slice_string[:2] #slicing it to the second element
print("The answer to 5.d is: ", slice_string)

four_b.append(type(slice_string)) # its not said which type I should appened, so I appended type of slice_string
print("The answer to 5.e is: ", four_b)

five_f = [int(four_b[1]), int(four_b[3]), int(four_b[5]) ] #created list which contained all possible integers from four_b
print("The answer to 5.f is: ", five_f)

four_b.append(type(five_f)) #its not said in the task which type I should append so I appened type of five_f
print("The answer to 5.g is: ", four_b)

four_b.append(type(three_setA))
print("The answer to 5.h is: ", four_b)
#Hello, since it wasn't mentioned in most tasks, every method which I was supposed to perform I performed on the first variable of certain type (except the exercise 4). If it was said to do method on set I did on the first one I created, not the last changed version where I appended or changed anything
four_b.append(type(three_setA))
print("The answer to 5.h is: ", four_b)
#Hello, since it wasn't mentioned in most tasks, every method which I was supposed to perform I performed on the first variable of certain type (except the exercise 4). If it was said to do method on set I did on the first one I created, not the last changed version where I appended or changed anything
