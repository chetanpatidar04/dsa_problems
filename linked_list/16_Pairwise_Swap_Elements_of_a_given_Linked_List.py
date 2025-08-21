# Given a singly linked list, the task is to swap linked list elements pairwise.

# Examples:

# Input : 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL 
# Output : 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> NULL

# Reverse-a-Linked-List-in-groups-of-given-size-1
 


# Input : 1 -> 2 -> 3 -> 4 -> 5 -> NULL 
# Output : 2 -> 1 -> 4 -> 3 -> 5 -> NULL





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


################################## Pairwise swap of linked list ################################################ 
    def pair_wise_swap_data(self):
        if self.head == None:
            print("No element present in the list")
            return
        if self.head.next == None:
            print(self.head.data)
            return
        current = self.head
        temp_count = 1                
        while (current.next):
            prev = current
            current = current.next      
            temp_count += 1
            if temp_count == 2:
                temp = current.data             
                current.data = prev.data
                prev.data = temp
                temp_count = 0

    def pair_wise_swap_node(self):
        head = self.head
        if not head or not head.next:
            return head

        # New head will be the second node
        new_head = head.next

        prev = None
        current = head

        while current and current.next:
            next_node = current.next
            next_pair = next_node.next

            # Swap current and next_node
            next_node.next = current
            current.next = next_pair

            if prev:
                prev.next = next_node

            # Move to the next pair
            prev = current
            current = next_pair
        self.new_head = new_head
        return new_head

    def print_list(self):
        head = self.new_head
        current = head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def traverse(self):
        current = self.head
        while(current.next):
            print(str(current.data) + " --> ",end="")
            current = current.next
        print(current.data)

          



linked_list = linked_list()
linked_list.head = node(10)
linked_list.head.next = node(20)
linked_list.head.next.next = node(30)
linked_list.head.next.next.next = node(40)
linked_list.head.next.next.next.next = node(50)
linked_list.head.next.next.next.next.next = node(60)
linked_list.traverse()
# linked_list.pair_wise_swap_data()
linked_list.pair_wise_swap_node()
linked_list.print_list()