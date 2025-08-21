# Input: head: 1 -> 2 -> 3 ->1  -> 4 -> NULL, key = 1 
# Output: 1 -> 2 -> 3 -> 4 -> NULL

# Input: head: 1 -> 2 -> 3 -> 4 -> 5 -> NULL , key = 3
# Output: 1 -> 2 -> 4 -> 5 -> NULL


# Approach:

# The idea is to traverse the linked list from beginning to end. While traversing, keep track of last occurrence key node and previous node of that key. After traversing the complete list, delete the last occurrence of that key.

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
    
    def travesal(self):
        if self.head:
            current = self.head
            count = 1
            while(current.next):
                print(str(current.data) + " --> ",end="")
                current = current.next
                count += 1
            print(current.data)

    def brute_force_to_delete_last_ocurance(self,key):
        if self.head:
            current = self.head
            count = 1
            key_count = 0
            while(current.next):
                if key == current.data:
                    key_count += 1
                current = current.next    
                count += 1
            current = self.head

            temp_count = 1
            new_key_count  = 0
            while(current.next):                
                if key == current.data:
                    new_key_count += 1
                    # print(new_key_count)
                    if new_key_count == key_count:
                        # print(current.data,prev_node.data)
                        prev_node.next = current.next
                        del current
                        current = prev_node
                temp_count += 1
                prev_node = current
                current = current.next
                print(current.data)    
        else:
            print("no element in stht list")

                    


########################## Optimzed code  ###################################################################################################### 
#    geeks for geeks


list = linked_list()
list.insert(10)
list.insert(20)
list.insert(30)
list.insert(40)
list.insert(10)
list.insert(60)
list.insert(40)
list.brute_force_to_delete_last_ocurance(10)
list.travesal()
# list.optimized_travese(1)
# list.optimized_travese(2)
# list.optimized_travese(3)
# list.delete_last_occurance(4)
# list.optimized_travese(5)
# list.optimized_travese(6)
