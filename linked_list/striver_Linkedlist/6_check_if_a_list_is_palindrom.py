class node():
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list():
    def __init__(self):
        self.head = None
    
    def insert_data(self,data):
        if self.head is None:
            self.head = node(data)
            return        
        current = self.head
        while(current.next):
            current = current.next
        current.next = node(data)
    

    def travesal(self,head=None):
        if head is None:
            head = self.head
            
        if head is None:
            print("No element present in linked list")
            return None
        if head.next is None:
            return head
        current = head        
        while(current):
            print(str(current.data) + " " ,end= "")
            current = current.next

# #  brute force with stack ========================================= 

    def check_palindrom(self):
        if self.head is None:
            print("No elements in the list")
            return None
        if self.head.next is None:
            print("list is a valid palindrom with one node ")
            return self.head
        st = []
        current = self.head
        while(current):
            st.append(current.data)
            current = current.next
        
        current1 = self.head
        while(current1):
            value = st.pop()
            if value != current1.data:
                print("list is not a valid palindrom")
                return self.head
            current1 = current1.next
        print("list is a valid palindrom")
        return self.head        

# Optimal solution ========================================= 
    # divide list into 2 equal parts and reverse the 2nd part and match with 1st part 
    def reverse(self,head):
        self.head = head
        if self.head == None:
            return
        current = self.head
        prev = None
        while(current):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            self.head = prev    
        return self.head

# Optimal_solution ==========================================

    def check_palindrom_optimal_sol(self):
        if self.head is None:
            print("no element in the list")
            return None
        if self.head.next is None:
            print(self.head.data)
            return self.head
        half_part2 = fast = current = self.head
        while(fast):
            # print("c ==> ",current.data,"f ==>",fast.data,half_part2.data)
            current = current.next
            if fast is None:
                half_part2 = current.next
                break
            if fast.next is None:
                half_part2 = current
                break
            else:
                half_part2 = current.next
            fast = fast.next.next
            half_part2 = self.reverse(half_part2)
            print("2nd revrse start")
            self.travesal(half_part2)
            print("2nd half2 end")

linked_list = linked_list()
linked_list.insert_data(10)
linked_list.insert_data(20)
linked_list.insert_data(30)
linked_list.insert_data(20)
linked_list.insert_data(10)
# linked_list.insert_data(40)
linked_list.travesal()
print()
print()
# linked_list.check_palindrom()
linked_list.check_palindrom_optimal_sol()
print()
print()
linked_list.travesal()