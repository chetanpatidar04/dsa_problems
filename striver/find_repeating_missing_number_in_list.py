# brute_force_approch

# # find_repeating_missing_number_in_list
li = [4,3,6,2,1,1]
n=6
repating_elem = []
missing = []
for i in range(len(li)):
    count = 0
    for j in range(i+1,len(li)):
        if li[i] == li[j]:
            repating_elem.append(li[j])
    if i + 1 not in li:  
        missing.append(i+1)
print(repating_elem,missing)



################################## Better Solution ######################################################
temp = [0,0,0,0,0,0]
li = [4,3,6,2,1,1]
n = 6
for i in range(n):
    temp[li[i]-1] = temp[li[i]-1] +1
for j in range(n):
    if temp[j] > 1:
        print("repating",li[j])
    elif temp[j] == 0:
        print("missing",li[j])      
