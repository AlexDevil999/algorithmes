

def recursion_sum(my_list):
    if len(my_list) != 0:
        return my_list[0] + recursion_sum(my_list[1:])
    return 0