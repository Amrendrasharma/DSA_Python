# Python Program to left rotate the array by d positions:

arr = [1,4,8,6]
d =2

for _ in range(d):
    first = arr[0]
    for i in range (len(arr)-1):
        arr[i]=arr[i+1]
    arr[-1]=first
print(arr)