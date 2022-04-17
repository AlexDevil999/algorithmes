


def merge_sort(my_list):
    
    if len(my_list) == 1:
        return my_list
    else:
        middle = len(my_list) // 2
        left = merge_sort(my_list[:middle])
        right = merge_sort(my_list[middle:])
        return merge_two_list(left,right)
        
        
        
def merge_two_list(a,b):
    c = []
    i = j = 0
    
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    
    return c
        