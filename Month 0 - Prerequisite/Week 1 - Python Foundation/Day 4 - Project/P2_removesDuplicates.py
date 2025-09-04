def remove_duplicates_with_loop(input_list):
    unique_list = []

    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

def remove_duplicates_set(li):
    unique_set = set(li)
    unique_list = list(unique_set)
    return unique_list

li = [2, 3, 4, 5, 2, 4]
print(remove_duplicates_set(li))