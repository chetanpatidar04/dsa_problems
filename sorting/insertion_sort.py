# li = [11,23,12,5,6]
# p1 = 0
# for i in range(1,len(li)):
#     temp = i
#     p1 = i - 1 
#     while (p1 >= 0 ):
#         print(li[temp] , li[p1])
#         if li[temp] < li[p1]:
#             li[temp],li[p1] = li[p1],li[temp]
#             temp -= 1
#         p1 -= 1    

# print(li)


# # without swaping

# # Python program for implementation of Insertion Sort

# # Function to sort array using insertion sort
# def insertionSort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1

#         # Move elements of arr[0..i-1], that are
#         # greater than key, to one position ahead
#         # of their current position
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

# # A utility function to print array of size n
# def printArray(arr):
#     for i in range(len(arr)):
#         print(arr[i], end=" ")
#     print()

# # Driver method
# if __name__ == "__main__":
#     arr = [12, 11, 13, 5, 6]
#     insertionSort(arr)
#     printArray(arr)



li = [23,1,10,5,2]

for i in range(len(li)):
    key = li[i]
    p1 = i - 1
    while( p1 >= 0 and key < li[p1]):
        li[p1+1] = li[p1]
        p1 -= 1
    li[p1+1] = key
print(li)