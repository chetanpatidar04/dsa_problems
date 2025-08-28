# Find Middle of the Linked List
# Last Updated : 14 Aug, 2025
# Given a singly linked list, the task is to find the middle node of the linked list.

# If the number of nodes is odd, return the middle node.
# If the number of nodes is even, there are two middle nodes, so return the second middle node.
# Example:

# Input: linked list: 1->2->3->4->5
# Output: 3 
# Explanation: There are 5 nodes in the linked list and there is one middle node whose value is 3.

# Input: linked list = 10 -> 20 -> 30 -> 40 -> 50 -> 60
# Output: 40
# Explanation: There are 6 nodes in the linked list, so we have two middle nodes: 30 and 40, but we will return the second middle node which is 40.

# Try it on GfG Practice
# redirect icon
# Middle-of-a-Linked-List4

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

    def find_the_middle_element(self):
        if self.head is None:
            return self.head
        current = self.head
        count = 0
        while(current):
            count += 1
            current = current.next

        current = self.head
        new_count = 0
        count = count // 2 
        while(current):
            new_count += 1 
            if count + 1 == new_count:
                print(" mid elem ==> ",current.data)
                return current.data
            current = current.next

# Optimal solution ==========================================================
    def find_the_middle_element_optiaml_solution(self):
        if self.head is None:
            return self.head
        if self.head.next is None:
            return self.head
        ptr1 = ptr2 = self.head
        while(ptr2 is not None and ptr2.next is not None):
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        print("==> ptr2 ",ptr1.data)
        return self.head


linked_list = linked_list()
head = linked_list.insert(10)
head = linked_list.insert(20)
head = linked_list.insert(30)
head = linked_list.insert(40)
head = linked_list.insert(50)
head = linked_list.insert(60)

linked_list.traversal(head)
linked_list.find_the_middle_element()
print("optimal solution")
linked_list.find_the_middle_element_optiaml_solution()
linked_list.traversal(head)
