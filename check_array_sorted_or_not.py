def sorted_or_not(arr):
    is_sorted = True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            is_sorted = False
            break
    return is_sorted
n = list(map(int,input("Enter a number seperated by space : ").split()))
print(sorted_or_not(n))   