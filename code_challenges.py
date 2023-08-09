def remove_every_other(my_list):
    
    for i, items in enumerate(my_list):
        if i%2==1:
            my_list.pop(i)
    return my_list

print