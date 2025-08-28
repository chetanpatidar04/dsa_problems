# Detect Cycle in Linked List
# Last Updated : 28 Aug, 2025
# Given the head of a singly linked list, determine whether the list contains a cycle.

# A cycle exists if, while traversing the list through next pointers, you encounter a node that has already been visited instead of eventually reaching nullptr.

# Examples:

# Input: head: 1 -> 3 -> 4 -> 3
# Output: true

# 3
 
# Explanation: The last node of the linked list does not point to NULL; instead, it points to an earlier node in the list, creating a cycle.

# Input: head: 1 -> 8 -> 3 -> 4 -> NULL 
# Output: false

# 4-
 
# Explanation: The last node of the linked list points to NULL, indicating the end of the list.

class node():
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list():
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        if self.head is None:
            self.head = node(data)
            return True
        current = self.head
        while(current.next):
            current = current.next
        current.next = node(data)
        return self.head
    
    def traversal(self,head):
        current = self.head
        while(current):
            print(" ===> "+ str(current.data),end="")
            current = current.next
        return self.head

# Brute Force approch ==========================================================

    def detect_cycle_in_list(self):
        if self.head is None:
            return self.head
        current = self.head
        st = []
        while(current):
            if current in st:
                print("Cycle detect",current.data)
                return self.head
            st.append(current)
            current = current.next
        print("No cycle in the loop")
        return self.head

# Optimal solution ==========================================================
    def detect_cycle_in_list_optimal_solution(self):
        if self.head is None:
            return self.head
        if self.head.next == None:
            return self.head.next
        ptr = ptr2 = self.head
        
        while(ptr2 and ptr2.next):
            ptr = ptr.next
            ptr2 = ptr2.next.next
            if ptr == ptr2:
                print("cycle detected ",ptr.data)
                return ptr
        print("no cycle detected optimal solution")
        return self.head


linked_list = linked_list()
head = node(1)
head.next = node(3)
head.next.next = node(4)
head.next.next.next = node(5)
head.next.next.next.next = head.next.next
linked_list.head = head

# linked_list.traversal(head)
head = linked_list.detect_cycle_in_list()
print("optimal solution")
linked_list.detect_cycle_in_list_optimal_solution()
# linked_list.traversal(head)
