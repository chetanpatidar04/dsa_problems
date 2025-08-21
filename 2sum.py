# optimal solution
li = [2,6,5,8,11]
li.sort()
target = 14
l = 0
r = len(li)-1
sum1 = 0
print (l,r)
while(l<=r):
    sum1 = li[l] + li[r]
    if sum1 == target:
        print(li[l],li[r])
    elif sum1 > target:
        r -= 1
    elif sum1 < target:
        l += 1 
        

# ## better approch
# li = [2,6,5,8,11,3]
# target = 14
# di ={}
# for i in range(len(li)):    
#     di[li[i]] = i
#     num = target - li[i]
#     if num in di:
#         print(i,di[num])





# ## bruteforce
# ## find the combination of the 2 number and return their index that will give target numbers
# li = [2,6,5,8,11,3]
# target = 14
# for i in range(len(li)):
#     for j in range(i,len(li)):
#         if target == li[i] + li[j]:
#             print(i,j)