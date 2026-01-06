def sum_avg(num):
    count = 0
    total = 0
    for _ in num:
        count+=1
    print("length of an array", count)
    for i in num:
        total += i
    print("Sum of the number",total)
    return "Average of numbers",total/count

n = list(map(int,input("Enter a number seperated by space").split()))
print(sum_avg(n))