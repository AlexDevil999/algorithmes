

def selection_sort(my_list):
    
    for i in range(0,len(my_list)-1):
        smallest = i
        for j in range(i+1,len(my_list)):
            if my_list[j] < my_list[smallest]:
                smallest = j
        my_list[i], my_list[smallest] = my_list[smallest],my_list[i]
        