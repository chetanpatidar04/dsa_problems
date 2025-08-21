li = [3,6,6,3,5,6,5,3,7,8,7,9]
for i in range(len(li)-1):
    for j in range(i+1,len(li)):
        if li[i] > li[j]:
            li[i],li[j] =li[j],li[i]
print(li)
