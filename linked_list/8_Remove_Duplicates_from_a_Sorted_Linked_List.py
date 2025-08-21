# # Remove Duplicates from a Sorted Linked List\
# Given a singly linked list. The task is to remove duplicates (nodes with duplicate values) from the given list (if it exists).
# Note: Try not to use extra space. The nodes are arranged in a sorted way.

# Examples:

# Input:
# LinkedList: 2->2->4->5
# Output: 2 -> 4 -> 5

# Explanation: In the given linked list 2 -> 2 -> 4 -> 5, only 2 occurs more than 1 time. So we need to remove it once.
# Input:
# LinkedList: 2->2->2->2->2
# Output: 2

# Explanation: In the given linked list  2 -> 2 -> 2 -> 2, 2 is the only element and is repeated 5 times. So we need to remove any four 2.





# Input: LinkedList: 1->2->3->4->5
# Output: 1->2->4->5
# Explanation:


 
# Input: LinkedList: 2->4->6->7->5->1
# Output: 2->4->6->5->1
# Explaination:


 
# Input: LinkedList: 7 
# Output: <empty linked list>

# [Naive Approach] Using Two-Pass Traversal - O(n) Time and O(1) space
# [Expected Approach] One-Pass Traversal with Slow & Fast Pointers - O(n) Time and O(1) Space

class node():
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list():
    def __init__(self):
        self.head = None

    def travesal(self):
        current = self.head
        while(current.next):
            print(str(current.data) + " --> ",end="")
            current = current.next
        print(current.data)


################################## Delete middle node from the list ################################################ 
    def remove_duplicate(self):
        if self.head:
            if self.head.next == None:
                return True
        count = 1
        current = self.head
        while(current.next):
            prev_node = current
            temp = current
            current = current.next
            if current.data == prev_node.data:
                prev_node.next = current.next
                current = prev_node
                del prev_node
            count += 1


          



linked_list = linked_list()
linked_list.head = node(10)
linked_list.head.next = node(10)
linked_list.head.next.next = node(30)
linked_list.head.next.next.next = node(40)
linked_list.head.next.next.next.next = node(40)
linked_list.head.next.next.next.next.next = node(40)
linked_list.travesal()
# linked_list.delete_mid_node()
linked_list.remove_duplicate()
linked_list.travesal()