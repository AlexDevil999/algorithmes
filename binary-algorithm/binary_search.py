
def binary_search(my_list,item):
    low,high = 0,len(my_list)-1
    while low <= item:
        mid = int((low+high)/2)
        print(mid)
        res = my_list[mid]
        print(res)
        if res > item:
            high = mid -1
        if res < item:
            low = mid + 1
        if res == item:
            return mid