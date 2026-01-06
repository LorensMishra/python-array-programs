def smallest(num):
    smallest = num[0]
    for i in num:
        if i<smallest:
            smallest = i
    return "Smallest element of the array:",smallest
n = list(map(int,input("Enter anumber seperated by space: ").split()))
print(smallest(n))