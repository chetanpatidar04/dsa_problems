class node():
    def __init__(self,data):
        self.data = data
        self.next = None

class link_list():
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
    
# ====================================== Brute force ================================================
def segregate_even_odd_node(head):
    list_1 = link_list()
    list_2 = link_list()
    if head is None:
        print("no element in the list")
        return None

    if head.next is None:
        return head
    count = 0
    current = head
    prev = None    
    while(current):
        count += 1
        if count % 2 != 0:
            list_1.insert(current.data)            
        else:
            list_2.insert(current.data)
        current = current.next
    
    if list_1.head is None:
        return list_2
    
    cur = list_1.head
    while(cur):
        prev = cur
        cur = cur.next
    
    prev.next = list_2.head
    return list_1.head


# ====================================== Brute force using array ================================================

def segregate_even_odd_nodes_using_list(head):
    li1 = []
    li2 = []
    current = head
    count = 0
    while(current):
        count += 1
        if count % 2 != 0:
            li1.append(current.data)
        else:
            li2.append(current.data)
        current = current.next

    li1 = li1 + li2
    linked_list_test = link_list()
    for i in li1:
        linked_list_test.insert(i)

    return linked_list_test.head    


# ====================================== Optimized solution ================================================
def optimized_sol(head):
    if head is None:
        return None
    if head.next is None:
        print("==>", head.data)
        return head

    # Dummy nodes to simplify logic
    odd_head = odd_tail = node(-1)
    even_head = even_tail = node(-1)

    current = head
    count = 1

    while current:
        next_node = current.next
        current.next = None  # Break original link

        if count % 2 != 0:
            odd_tail.next = current
            odd_tail = odd_tail.next
            print("odd_tail", odd_tail.data)
        else:
            even_tail.next = current
            even_tail = even_tail.next
            print("even_tail", even_tail.data)

        current = next_node
        count += 1

    # Connect odd list to even list
    odd_tail.next = even_head.next
    return odd_head.next

def traversal(head):
    if head is None:
        return
    if head.next is None:
        print(" this is a head")
        return head
    current = head
    while(current):
        print(" ==> " + str(current.data) , end= "")
        current = current.next
    return

link_list_temp = link_list()
head = link_list_temp.insert(10)
head = link_list_temp.insert(20)
head = link_list_temp.insert(30)
# link_list_temp.insert(40)
# link_list_temp.insert(50)
# head = link_list_temp.insert(60)
print(" asdf ======>>>")
traversal(head)
print()
print(" asdf ======>>>")

# final_list_head = segregate_even_odd_node(head)
# print(" final_list")
# list_head = segregate_even_odd_nodes_using_list(head)

odd_head = optimized_sol(head)
print(" rhis is a")
traversal(odd_head)
print(" evene_haes")
# traversal(even_head)
