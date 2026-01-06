def largest_number(num):
    largest = num[0]
    for i in num:
        if i>largest:
            largest = i
    return largest        

n = list(map(int,input("Enter a numbers seperated by space: ").split()))
print(largest_number(n))
# for loop runs once for each element in the array
# so time complexity of this ----> O(n)
# space complexity O(1) only one extra variable is used.
