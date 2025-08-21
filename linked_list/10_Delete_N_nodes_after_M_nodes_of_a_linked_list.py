# Given a linked list and two integers m and n, the task is to traverse the linked list such that you skip m nodes, then delete the next n nodes, and continue the same till end of the linked list.
# Note: m cannot be 0.
# Example: 

# Input: Linked List: 9->1->3->5->9->4->10->1, n = 1, m = 2
# Output: 9->1->5->9->10->1
# Explanation: Deleting 1 node after skipping 2 nodes each time, we have list as 9-> 1-> 5-> 9-> 10-> 1.

# Input: Linked List: 1->2->3->4->5->6, n = 1, m = 6 
# Output: 1->2->3->4->5->6 
# Explanation: After skipping 6 nodes for the first time , we will reach of end of the linked list, so, we will get the given linked list itself.




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
    def remove_n_nodes_after_m_nodes(self,m,n):
        if self.head:
            if self.head.next == None:
                return True
        count = 1
        current = self.head
        while(current.next):
            prev_node = current
            current = current.next
            if count == m:
                while(n):
                    prev_node.next = current.next
                    current = prev_node
                    current = current.next
                    if current.next ==None:
                        prev_node.next = None
                        break
                    n -= 1
            count += 1


linked_list = linked_list()
linked_list.head = node(10)
linked_list.head.next = node(20)
linked_list.head.next.next = node(30)
linked_list.head.next.next.next = node(40)
linked_list.head.next.next.next.next = node(50)
linked_list.head.next.next.next.next.next = node(40)
linked_list.travesal()
linked_list.remove_n_nodes_after_m_nodes(m=2,n=4)
linked_list.travesal()