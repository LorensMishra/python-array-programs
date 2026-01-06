def second_smallest_num(arr):
    if len(arr)<2:
       return "Second smallest not posible"
    smallest = second_smallest = float('inf') 
    for i in arr:
       if i<smallest:
           second_smallest=smallest
           smallest = i
       elif i<second_smallest and i != smallest:
           second_smallest = i
    if second_smallest == float('inf'):
        return "No smallest element"
    return second_smallest

num = list(map(int,input().split()))
print(second_smallest_num(num))
