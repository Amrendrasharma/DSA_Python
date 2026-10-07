# Array Reverse

arr=[1,4,5,6,7]

left = 0
right = len(arr) -1

while left < right:
    arr[left],arr[right] = arr[right],arr[left]
    left +=1
    right -=1
print(arr)


#By using class

class Solution:
    def reverseArray(self, arr):
        # code here
        l=0
        r= len(arr) - 1
        while l < r:
            arr[l],arr[r]=arr[r],arr[l]
            l +=1
            r -=1
        return arr
if __name__ == "__main__":
    arr=[1,2,7,5,4]
    obj = Solution()
    print(obj.reverseArray(arr))