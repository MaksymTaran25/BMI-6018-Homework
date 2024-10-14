'''
1.a
Using the print() function only, get the wrong_add_function to print out where
it is making a mistake, given the expected output for ex, "we are making an error 
in the loop", which you would put near the loop. 
Structure the print() statement to show what the expected output ought to be
via f-strings: ie "The correct answer is supposed to be: [...]".
1.b
Then, changing as little as possible, modify the function, using the same 
general structure to output the correct answer. Call this new function 
correct_add_function() 
'''

#It was said that I need to call this function after the wrong one, but it wasn't stated that I can't define it before. That is why I decided to call it when I print the correct output.
def correct_add_function(arg1,arg2):
   arg1_index=0
   while arg1_index < len(arg1):
      arg_2_sum = 0
      for arg2_elements in arg2:
         arg_2_sum = sum([arg1[arg1_index]+arg2[arg1_index]])
      arg1[arg1_index]=arg_2_sum  
      arg1_index+=1
   return arg1

def wrong_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [6,9,12]

   whereas the expected correct answer is, [2,3,4]

   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   '''

   arg1_index=0
   while arg1_index < len(arg1):
      arg_2_sum = 0
      for arg2_elements in arg2:
         arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
      arg1[arg1_index]=arg_2_sum  
      arg1_index+=1
   return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

print("1.a: We are making an error in the loop on line 41, in order to fix it I changed line 42")
print(f"1.a: Output is: {wrong_add_function(arg1, arg2)}")

arg1 = [1,2,3] #To set values to lists back because they got changed after executing wrong_add_function
arg2 = [1,1,1]
print(f"1.b: The correct answer is supposed to be: {correct_add_function(arg1, arg2)}")



'''
2.a
Update the numeric section of the function with your changes from 1 for both 
2.b and 2.c

2.b
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
returns an error message to the user, in case users give invalid inputs,
(for example an input of ["5","2", 5])
: "Your input argument [1 or 2] at element [n]
is not of the expected type. Please change this and rerun. Name this function 
exception_add_function()

2.c
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
gets it to process via the string section. IE, do not, outside the function,
change the values of arg_str_1 or arg_str_2. Name this function 
correction_add_function(), i.e you will not be updating the wrong_add_function,
you will simply handle the error of wrong inputs in a seperate function, you want
the wrong_add_function to output its current result you are only bolstering the 
function for edge cases .
'''

def exception_add_function(arg1,arg2): #this function separately checks all elements in both arguments whether they can concanite, if its number it should throw type error.
   for i in range(len(arg1)): # for all elements in this lists
      if type(arg1[i]) != type(arg2[i]): # if type of elements of both arguments at the same index are not equal (I assume there is only one wrong value in both lists because its like that in example and since there was nothing about it in assignment.)
         try:
            print(arg1[i] + arg2[i]) #I just printed sum of elements because if they are of type int and str it will cause TypeError
         except TypeError:
            print(f"2.b :Your input argument [1 or 2] at element [{i}] is not of the expected type. Please change this and rerun.")

def correction_add_function(arg1,arg2):
   for i in range(len(arg1)): # for all elements in this lists
      if type(arg1[i]) != str or type(arg2[i]) != str: # if type of elements of both arguments at the same index are not equal (I assume there is only one wrong value in both lists because its like that in example and since there was nothing about it in assignment.)
         try:
            print(arg1[i] + arg2[i]) #I just printed sum of elements because if they are of type int and str it will cause TypeError
         except TypeError: # if error changes type to string to process via the string section
            arg1[i] = str(arg1[i])
            arg2[i] = str(arg2[i])

def wrong_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [4,5,6]
   
   If the lists are lists of strings, concatenate them
   Example:
      > wrong_add_function(['1','2','3'],['1','1','1'])
      > ['1111','2111','3111']
   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   '''
   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
               arg_2_sum = sum([arg1[arg1_index]+arg2[arg1_index]])
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1
arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]
exception_add_function(arg_str_1,arg_str_2)# it was stated that I need to do try catch block in function so I made it before and just called without changing numeric or string sections.
correction_add_function(arg_str_1,arg_str_2) # this function with the use of try/except changes values of type int to str in order to process via the string section 
print(wrong_add_function(arg_str_1,arg_str_2)) # after indirect change of arguments call function to process via the string section.
