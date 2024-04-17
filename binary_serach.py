### binary serach

import array

arr = array.array('b', [1, 29, 12, 49, 4, 3, 5, 16, 22])
def binary_search(element, arr):
    arr = sorted(arr)
    found_flag = False
    i = 0
    j = len(arr) - 1
    while found_flag == False:
        mid = i + (j - i) // 2
        if arr[mid] == element:
            found_flag = True
            return mid
        elif element < arr[mid]:
            j = mid - 1
        else:
            i = mid + 1
    return -1

index_found = binary_search(16, arr)
if index_found == -1:
    print('Element does not exist in the array.')
else:
    print(f'The target element has found on the index {index_found}!')  