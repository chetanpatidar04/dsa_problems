# Input: 1 -> 2 -> 3 -> 4, N = 3
# Output: 2
# Explanation: Node 2 is the third node from the end of the linked list.

# Input: 35 -> 15 -> 4 -> 20, N = 4
# Output: 35
# Explanation: Node 35 is the fourth node from the end of the linked list.


# [Naive Approach] By Finding the length of list - Two Pass - O(M) Time and O(1) Space
# [Expected Approach] Using Two Pointers - One Pass - O(M) Time and O(1) Space

class node():
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list():
    def __init__(self):
        self.head = None

    def insert(self,data):
        if self.head == None:
            self.head = node(data)
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = node(data)
    
    def travesal(self,n):
        if self.head:
            current = self.head
            count = 1
            while(current.next):
                print(str(current.data) + " --> ",end="")
                current = current.next
                count += 1
            print(current.data)
            new_count = count - n - 1
            temp = 1
            current = self.head
            while(current.next):
                current = current.next                
                if temp > new_count:
                    print("Nth node form the last",current.data)               
                    break
                temp += 1
                    


########################## Optimzed code  ###################################################################################################### 
#    geeks for geeks


list = linked_list()
list.insert(10)
list.insert(20)
list.insert(30)
list.insert(40)
list.insert(50)
list.insert(60)
# list.travesal(6)
# list.optimized_travese(1)
# list.optimized_travese(2)
# list.optimized_travese(3)
list.optimized_travese(4)
# list.optimized_travese(5)
# list.optimized_travese(6)
