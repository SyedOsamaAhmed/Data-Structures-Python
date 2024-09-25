import math
arr=[1,3,5,6]

def binarySearch(arr,target):
    low = 0
    high = len(arr) - 1
    mid = 0
    while (low < high):
        mid = (high+low)//2
        if(arr[mid]<target):
            low=mid+1
        elif arr[mid]>target:
            high=mid-1
        else:
            return mid
       

    return -1
print(binarySearch(arr,7))