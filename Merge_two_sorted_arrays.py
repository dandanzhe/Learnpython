def merge_arrays(arr1, arr2):
    for i in arr1:
        arr2.append(i)
    b=set(arr2)
    return sorted(list(b))
print merge_arrays([1,2,3,4], [5,-20,6,7,8])