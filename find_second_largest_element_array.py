def sec_largest(num):
    large=num.sort()
    return num[1]
n = list(map(int,input().split()))
print(sec_largest(n))