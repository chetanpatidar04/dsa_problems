# Input: linked list = 10 -> 20 -> 30 -> 40 -> 50, 
# k = 4
# Output: 50 -> 10 -> 20 -> 30 -> 40

# Explanation: After rotating the linked list to the left by 4 places, the 5th node, i.e node 50 becomes the head of the linked list and next pointer of node 50 points to node 10.

# Input: linked list = 10 -> 20 -> 30 -> 40, k = 6
# Output: 30 -> 40 -> 10 -> 20 




# [Naive Approach] Shifting head node to the end k times - O(n * k)) Time and O(1) Space
# [Expected Approach] By changing pointer of kth node - O(n) Time and O(1) Space


class node:
    def __init__(self,data):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None


############################################## Insert at the end of Linked List ############################################################################################

    def insert_at_end(self,data):
        if self.head is None:
            self.head = node(data)
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = node(data)

############################################## insert at the Beginning of Linked List ############################################################################################
    def insert_at_beginning(self,data):
        if not self.head:
            self.head = node(data)
            return True
        temp = self.head
        self.head = node(data)        
        self.head.next = temp


############################################## insert at the specific position of Linked List ############################################################################################
    def insert_at_specific_position(self,data,pos):
        if self.head:
            count = 1
            current = self.head
            while(current.next):
                count += 1
                temp = current.next
                if count == pos:          
                    new_node = node(data)
                    current.next = new_node
                    new_node.next = temp
                current = current.next


    def traverse(self):
        current = self.head
        while(current.next):
            print(str(current.data) + " --> ",end="")
            current = current.next
        print(current.data)

    def rotate_list(self,k):
        if self.head:
            if self.head.next is None and k > 1:
                print("Only 1 node is present")
                return True
        current = self.head
        count = 1
        end_node = None
        new_head = None
        while(current.next):
            if k == 0:
                print("can not rotate list")
                break
            if k == count:
                print(current.data)
                end_node = current
                new_head = end_node.next
            current = current.next            
            count += 1
            
            if current.next == None and  k > count:
                k = k % count
                count = 1
                current = self.head
        if end_node is not None: 
            end_node.next = None
            current.next = self.head
            self.head = new_head

linked_list = linked_list()
linked_list.insert_at_end(20)
linked_list.insert_at_end(40)
linked_list.insert_at_end(50)
linked_list.insert_at_end(60)
linked_list.insert_at_beginning(10)
linked_list.insert_at_specific_position(30,3)
linked_list.traverse()
linked_list.rotate_list(12)
linked_list.traverse()

