# def merge(left, right):
#     merged = []
#     i = j = 0

#     # Merge the two halves by comparing elements
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             j += 1

#     # Append remaining elements
#     merged.extend(left[i:])
#     merged.extend(right[j:])
#     return merged

# low = 0
# li = [3,1,5,9,4,6,2,8]
# def merge_sort (arr1):
#     low = 0
#     high = len(arr1)
#     print(low,high)
#     if len(arr1) <= 1:
#         return arr1
#     mid = len(arr1) // 2
#     left = merge_sort(arr1[low:mid])
#     right = merge_sort(arr1[mid:high])
#     arr1 = merge(left,right)
#     return merge(left,right)

# print(merge_sort(li))

def merge(left,right):
    print(left,right)
    i = j = 0
    merge_li = []    
    while( i < len(left) and j < len(right)):
        if left[i] < right[j]:
            merge_li.append(left[i])
            i = i + 1  
        else:
            merge_li.append(right[j])
            j = j + 1
    merge_li.extend(left[i:])
    merge_li.extend(right[j:])
    return merge_li

li =[3,1,5,9,4,6,2,8,8] 
def merge_sort(li):
    if len(li) <= 1:
        return li
    mid = len(li) // 2
    left = merge_sort(li[0:mid])
    right = merge_sort(li[mid:])
    return merge(left,right)

print(merge_sort(li))


