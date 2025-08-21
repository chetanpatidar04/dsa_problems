li = [23,12,434,1,3,45,78]
p1 = len(li)
for i in range(len(li)):
    swaped = False
    for j in range(0,len(li)-1-i):
        if li[j] > li[j+1]:
            li[j],li[j+1] = li[j+1],li[j]
            swaped = True
    if not swaped:
        break
print(li)
