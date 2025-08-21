# ques :- Given the head of a linked list where nodes can contain values 0s, 1s, and 2s only. Your task is to rearrange the list so that all 0s appear at the beginning, followed by all 1s, and all 2s are placed at the end.

# Input: head = 1 → 2 → 2 → 1 → 2 → 0 → 2 → 2

# Output: 0 → 1 → 1 → 2 → 2 → 2 → 2 → 2

# Explanation: All the 0s are segregated to the left end of the linked list, 2s to the right end of the list, and 1s in between.

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
            return self.head
        current = self.head
        while(current.next):
            current = current.next
        current.next = node(data)
        return self.head
    

    def traversal(self,head):
        if head is None:
            return None
        if head.next is None:
            return head
        current = head
        while(current):
            print(" ==> " + str(current.data),end="")
            current = current.next
        return head

# ================================ brute force =============================================================================
    def sort_list(self,head):
        if head is None:
            return head
        if head.next is None:
            return head
        current = head
        count1 = 0
        count0 = 0
        count2 = 0
        while(current):
            if current.data == 1:
                count1 += 1
            if current.data == 0:
                count0 += 1
            if current.data == 2:
                count2 += 1
            current = current.next

        print(count0,count1,count2)
        current = head
        temp_count = 1
        while(current):
            if count0 != 0:
                current.data = 0
                count0 -= 1

            elif count1:
                current.data = 1
                count1 -= 1

            elif count2:
                current.data = 2
                count2 -= 1

            temp_count += 1   
            current = current.next
        return head

# ================================ optimized solution =================================================================================
    def sort_list_optmized(self,head):
        
        if head is None:
            return head
        if head.next is None:
            return head
        current = head
        head0 = tail_head0 = node(-1)
        head1 = tail_head1 = node(-1)
        head2 = tail_head2 = node(-1)
        
        while(current):
            next_node = current.next
            current.next = None
            if current.data == 0:
                tail_head0.next = current
                tail_head0 = tail_head0.next
                
            elif current.data == 1:
                tail_head1.next = current
                tail_head1 = tail_head1.next
            elif current.data == 2:
                tail_head2.next = current
                tail_head2 = tail_head2.next
            current = next_node
        
        tail_head0.next  = head1.next
        tail_head1.next = head2

        return head0.next


linked_list = linked_list()
head = linked_list.insert(0)
head = linked_list.insert(1)
head = linked_list.insert(0)
head = linked_list.insert(1)
head = linked_list.insert(0)
head = linked_list.insert(2)
head = linked_list.insert(2)
head = linked_list.insert(0)
head = linked_list.insert(0)
head = linked_list.insert(0)

linked_list.traversal(head)
# linked_list.sort_list(head)
print("this is sorted")
head = linked_list.sort_list_optmized(head)
linked_list.traversal(head)