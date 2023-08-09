def remove_every_other(my_list):
    new_list = []
    for i, items in enumerate(my_list):
        if i%2==0:
            new_list.append(items)
    return new_list

print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))