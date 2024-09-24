#Insertion in any position unsorted array:

# array = [2, 4, 1, 8, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
# pos=2
# num=10
# n=5


# def insertInArray(array,pos,num,n):

#     for i in range(n-1,pos-1,-1):
#         array[i+1]=array[i]
       
        

#     array[pos]=num

#     return array


# print(insertInArray(array,pos,num,n))



# Deletion in unsorted array:
arr = [10, 50, 30, 40, 20]
key = 30

def findElemnent(key):
    for i in range(0,len(arr)-1):
        if arr[i]==key:
            return key
    
    return -1

pos=findElemnent(key)

if(pos>-1):
    arr.remove(pos)
    print(arr) 
   
   

else:
    print("Key not found!")
