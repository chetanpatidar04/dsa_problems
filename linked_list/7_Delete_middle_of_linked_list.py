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
    def delete_mid_node(self):
        if self.head:
            if self.head.next == None:
                self.head = None
                return
        current = self.head
        count = 1
        while(current.next):
            current = current.next
            count += 1
        n = count // 2
        current = self.head
        new_count = 1
        while(current.next):
            prev_node = current
            current = current.next
            if new_count == n + 1:
                prev_node.next = current.next
                del current
                current = prev_node                
            new_count += 1    



linked_list = linked_list()
linked_list.head = node(10)
linked_list.head.next = node(20)
linked_list.head.next.next = node(30)
linked_list.head.next.next.next = node(40)
linked_list.head.next.next.next.next = node(50)
linked_list.head.next.next.next.next.next = node(60)
linked_list.travesal()
# linked_list.delete_mid_node()
linked_list.two_pointer_approch_to_del_mid_node()
linked_list.travesal()