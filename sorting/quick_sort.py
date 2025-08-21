# li = [4,3,1,2,5,9,7,10,6]
# def temp(left,right,mid):
#     new_left = []
#     new_rig = []
#     print(left,right,mid)
#     if len(left) > 1:
#         for i in left: 
#             if i !=[]:           
#                 if i <= mid:
#                     new_left.append(i)
#                 else:
#                     new_rig.append(i)
               
#     if len(right) > 1:
#         for i in right:
#             if i != []:
#                 if i <= mid:
#                     new_left.append(i)
#                 else:
#                     new_rig.append(i)         
#     return new_left + new_rig

# def quick_sort(li): 
#     if len(li) <= 1:
#         return li
#     mid = len(li)//2
#     t = li[mid]
#     left = quick_sort(li[:mid])
#     right = quick_sort(li[mid:])
#     return temp(left,right,t)

# print(quick_sort(li))
# # print(temp([4,3,1,2],[9,7,10,6],5))