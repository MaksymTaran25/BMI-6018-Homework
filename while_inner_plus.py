input_list = [1,2,3,4,[5,6,7,[8,9],2],2,4]

#My idea was to implement method: count_items which counts all the integers in input_list and then use it for my while statement to compare amount of items in list and amount of integers
#In order to get to the integers of the most deep list I had to make clear while statement at line 16 to compare length of list with amount of all integers, if we already got to the deepest list the amount will be the same, if not the deepest list will be counted as 1 in the length which means that length of list will be less then amount of all integers

def count_items(provided_list): # function to count all integers
    count = 0
    for item in provided_list:
        if isinstance(item, list): # if item in list is of type list
            count += count_items(item) # count = count integers inside this list (recursion)
        else: # if item is integer
            count += 1 
    return count

while len(input_list) != count_items(input_list): # using while to compare length of list with amount of  all integers in all lists
    while isinstance(input_list[0], int): # if there are int elements in provided list 
        input_list.remove(input_list[0]) # remove them from the list
    while isinstance(input_list[-1], int): # if there are int elements in the end ofprovided list 
        input_list.remove(input_list[-1]) # remove them from the list
    copy_list = input_list.copy() # I created copy of the list
    input_list.clear() # cleared original list to modify after
    for sublist in copy_list: # for lists in main list
        for item in sublist: #for items in this lists
            input_list.append(item) # append to cleared version of original list

for i in range(len(input_list)): # here I add 1 to every element of the most deep list from original "input_list"
    input_list[i] += 1

print(input_list)
