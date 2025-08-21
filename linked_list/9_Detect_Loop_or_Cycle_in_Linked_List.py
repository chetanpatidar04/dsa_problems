# Given a singly linked list, check if the linked list has a loop (cycle) or not. A loop means that the last node of the linked list is connected back to a node in the same list.

# Examples:

# Input: head: 1 -> 3 -> 4 -> 3
# Output: true


 
# Input: head: 1 -> 8 -> 3 -> 4 -> NULL 
# Output: false

# [Naive Approach] Using HashSet - O(n) Time and O(n) Space
# [Expected Approach] Using Floyd's Cycle-Finding Algorithm - O(n) Time and O(1) Space



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
    def detect_cycle(self):
        st = set()
        if self.head:
            if self.head.next == None:
                return True
        current = self.head
        while(current.next):
            if current not in st:
                st.add(current)
            else:                
                return True
            current=current.next    
        return False
          

    def floyds_algo(self):
        if self.head:
            slow = self.head
            fast = self.head
            while(slow and fast.next and fast.next.next):
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
        return False    


linked_list = linked_list()    
   # Create a hard-coded linked list:
    # 1 -> 3 -> 4
linked_list.head = node(1)
linked_list.head.next = node(3)
linked_list.head.next.next = node(4)

# Create a loop
# linked_list.head.next.next.next = linked_list.head.next


# linked_list.travesal()
print(linked_list.detect_cycle())
print(linked_list.floyds_algo(),"floyds")
# linked_list.travesal()
