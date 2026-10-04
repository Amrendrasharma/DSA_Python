# Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.

# Note: If the second largest element does not exist, return -1
    
def getSecondLargest(arr):
    n= len(arr)
    arr.sort(reverse=True)
    largest = -1
    secondlargest = -1
    for i in range(n):
        if arr[i] > largest:
            largest=arr[i]
        elif arr[i] > secondlargest and arr[i] != largest:
            secondlargest = arr[i]
    return secondlargest

if __name__ == "__main__":
    arr = [15, 12, 16, 9,16]
    print(getSecondLargest(arr))
