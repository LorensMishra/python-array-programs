def copy_array(arr):
    arr2 = []
    for i in arr:
        arr2.append(i)
    return arr2
n = list(map(int,input().split()))
print(copy_array(n))