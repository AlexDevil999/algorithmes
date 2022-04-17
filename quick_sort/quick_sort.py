


def quick_sort(my_list):
    if len(my_list) < 2:
        return my_list
    else:
        mountain = my_list[0]
        less = [i for i in my_list[1:] if i < mountain]
        greater = [i for i in my_list[1:] if i > mountain]
        return quick_sort(less) + [mountain] + quick_sort(greater)