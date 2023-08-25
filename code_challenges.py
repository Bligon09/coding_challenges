# def remove_every_other(my_list):
#     new_list = []
#     for i, items in enumerate(my_list):
#         if i%2==0:
#             new_list.append(items)
#     return new_list

# print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# def filter_list(l):
#     'return a new list with the strings filtered out'
#     new_list=[]
#     for element, i in  enumerate(l):
#         if isinstance(i, int)== True:
#             new_list.append(i)

#     return new_list

# print(filter_list([1,'a','b',0,15]))

# def descending_order(num):
#     # Bust a move right here
#     # take a non-negative number, and return it with its digits in descending order
#     # example: 12345 should return 54321
#     num_list=[]
#     num_str=str(num)
#     new_str=""
    
#     for element in num_str:
#         num_list.append(element)
        
#     num_list.sort()
#     num_list.reverse()
    
#     for num in num_list:
#         new_str+=num
        
#     return(int(new_str))

def areYouPlayingBanjo(name):
    # Create a function which answers the question "Are you playing banjo?".
    # If your name starts with the letter "R" or lower case "r", you are playing banjo!


    cap_name=name.upper()

    if cap_name.startswith('R')==True:
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'