
# Move all Zeros to End of Array

arr =[1,1,0,1,8,6,0,8]

n = len(arr)
non_zero=[]
no_zero=[]
for i in range(n):
    if arr[i] !=0:
        non_zero.append(arr[i])
    else:
        no_zero.append(arr[i])
updated_arr = non_zero + no_zero
print(updated_arr)