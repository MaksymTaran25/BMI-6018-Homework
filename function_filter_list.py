given_list = [1,2,3,4,5,6,7,8,9] # creating list
def filter_list(list, threshold): #defining function with two arguments
    while len(list) != threshold: # if length of list does not equal to threshold
        list.remove(list[-1]) # remove last item of the list until it will be equal
    print(list)

filter_list(given_list, 6) # calling function