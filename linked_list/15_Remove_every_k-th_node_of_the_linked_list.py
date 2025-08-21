# Given a singly linked list, the task is to remove every kth node of the linked list. Assume that k is always less than or equal to the length of the Linked List.
# Examples : 

# Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6, k = 2
# Output: 1 -> 3 -> 5 
# Explanation: After removing every 2nd node of the linked list, the resultant linked list will be: 1 -> 3 -> 5 .

# Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10, k = 3
# Output: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10
# Explanation: After removing every 3rd node of the linked list, the resultant linked list will be: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10.

class node():
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list():
    def __init__(self):
        self.head = None
    

    def travesal(self):
        if self.head is None:
            print("No elements in the list")
            return
        current = self.head
        while(current.next):
            print(str(current.data)," ==> ",end="")
            current = current.next
        print(current.data)         

    def nth_node(self,n):
        if self.head is None:
            print("No elements in the list")
            return
        count = 1
        temp = 0
        
        current = self.head
        print(str(current.data),end="")   
        while(current.next):
            if n == temp:
                print(" ==> "+str(current.data),end="")                
                temp = 0
            current = current.next    
            temp += 1
            count += 1 



linked_list = linked_list()
linked_list.head = node(10)
linked_list.head.next = node(20)
linked_list.head.next.next = node(30)
linked_list.head.next.next.next = node(40)
linked_list.head.next.next.next.next = node(50)
linked_list.head.next.next.next.next.next = node(40)
linked_list.travesal()
linked_list.nth_node(2)