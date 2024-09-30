input_list = [1,2,3,4,[5,6,7,[8,9],2],2,4]

#The programm is the same as the while_inner_plus but instead of doing while statement, I created fuction which does the same and calls itself

def minimize_list(list): #function to remove integers and get to the deeper list
    while isinstance(list[0], int): # if there are int elements in provided list 
        list.remove(list[0]) # remove them from the list
    while isinstance(list[-1], int): # if there are int elements in the end ofprovided list 
        list.remove(list[-1]) # remove them from the list
    copy_list = list.copy() # I created copy of the list
    list.clear() # cleared original list to modify after
    for sublist in copy_list: # for lists in main list
        for item in sublist: #for items in this lists
            list.append(item) # append to cleared version of original list
    
    while len(input_list) != count_items(input_list): 
        minimize_list(input_list) # function calls itself (recursion)
    
def count_items(provided_list): # function to count all integers
    count = 0
    for item in provided_list:
        if isinstance(item, list): # if item in list is of type list
            count += count_items(item) # count = count integers inside this list (recursion)
        else: # if item is integer
            count += 1 
    return count

minimize_list(input_list) #calling function

for i in range(len(input_list)): # here I add 1 to every element of the most deep list from original "input_list"
    input_list[i] += 1

print(input_list)
