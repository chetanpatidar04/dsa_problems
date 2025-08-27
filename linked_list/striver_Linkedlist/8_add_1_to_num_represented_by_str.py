# Add 1 to a Linked List Number
# Difficulty: MediumAccuracy: 31.91%Submissions: 333K+Points: 4Average Time: 20m
# You are given a linked list where each element in the list is a node and have an integer data. You need to add 1 to the number formed by concatinating all the list node numbers together and return the head of the modified linked list. 

# Note: The head represents the first element of the given array.

# Examples :

# Input: LinkedList: 4->5->6
# Output: 457

# Explanation: 4->5->6 represents 456 and when 1 is added it becomes 457. 
# Input: LinkedList: 1->2->3
# Output: 124
 
# Explanation:  1->2->3 represents 123 and when 1 is added it becomes 124. 
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)


class node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
class link_list():
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        if self.head is None:
            self.head = node(data)
            return self.head
        current = self.head
        while(current.next):
            current = current.next
        current.next = node(data)
        return self.head
        
    def travsal(self,head):
        if head is None:
            print("No head present")
            return None
        if head.next is None:
            print("==> "+ str(head.data),end="")
            return head

        current = head
        while(current):
            print(" ==> "+ str(current.data),end="")
            current = current.next
        return head

    def reverse(self,head):    
        if head == None:
            return
        current1 = self.head
        prev = None
        while(current1):
            next_node = current1.next
            current1.next = prev
            prev = current1
            current1 = next_node
            self.head = prev    
        return self.head

#  Brute Force solution =======================================>
    def add_1_num(self):
        new_head = self.reverse(self.head)
        current = new_head
        carry = 1
        while(current):
            if carry <= 0:
                head = self.reverse(new_head)
                return head            
            new_data = (current.data + carry) % 10
            carry  = (current.data + carry) // 10
            current.data = new_data
            if current.next is None and carry > 0:
                current.next = node(carry)
                current.next = node(carry)
                carry = 0
            current = current.next
        head = self.reverse(new_head)  
        return head

linked_list = link_list()
head = linked_list.insert(9)
head = linked_list.insert(9)
head = linked_list.insert(8)

linked_list.travsal(head)
print()
temp = linked_list.add_1_num()
print("Adfs df")
linked_list.travsal(temp)