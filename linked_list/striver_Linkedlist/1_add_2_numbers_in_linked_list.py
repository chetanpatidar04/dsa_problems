# # leetcode solution
# def addTwoNumbers(
#         self, l1: Optional[ListNode], l2: Optional[ListNode]
#     ) -> Optional[ListNode]:
#         dummyHead = ListNode(0)
#         curr = dummyHead
#         carry = 0
#         while l1 != None or l2 != None or carry != 0:
#             l1Val = l1.val if l1 else 0
#             l2Val = l2.val if l2 else 0
#             columnSum = l1Val + l2Val + carry
#             carry = columnSum // 10
#             newNode = ListNode(columnSum % 10)
#             curr.next = newNode
#             curr = newNode
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#         return dummyHead.next






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
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = node(data)

def traversal(head):
    if head is None:
        print("No head")
        return head
    if head.next is None:
        print(head.data)
        return head
    current = head
    while(current):
        print(" ==> " + str(current.data) ,end="")
        current = current.next
    return True

link_list3 = link_list() 



link_list1 = link_list()

link_list1.insert(3)
link_list1.insert(5)
# link_list.insert(30)
# link_list.insert(40)
# link_list.insert(50)
traversal(link_list1.head)

link_list2 = link_list()
print()
link_list2.insert(4)
link_list2.insert(5)
link_list2.insert(9)
link_list2.insert(9)
# link_list2.insert(50)
traversal(link_list2.head)


def addrt(head1,head2):
    print(head1.data,"data",head2.data)
    carry = 0
    t1 = head1
    t2 = head2
    print(t1.data,"datae",t2.data)
    sum = None
    while(t1 or t2):
        # print(t1.data)
        # return
        tmp1 = 0
        tmp2 = 0
        if t1 is not None:
            tmp1 = t1.data
            
        if t2 is not None:
            tmp2 = t2.data
        
        carry,value = addt(tmp1,tmp2,carry)
        link_list3.insert(value)
        print(value,"l3_data")
        if t1 is not None:
            t1 = t1.next
        if t2 is not None:
            t2 = t2.next
    if carry:
        link_list3.insert(carry)
    return link_list3.head         

def addt(t1_data,t2_data,carry):
    addit = t1_data + t2_data + carry
    value = addit % 10
    carry = addit // 10
    return carry,value





# ++++++++++++++++++++++++++ optmizied funtion ++++++++++++++++++++++++++


def add_two_numbers(head1, head2):
    dummy = node(0)
    current = dummy
    carry = 0

    while head1 or head2 or carry:
        val1 = head1.data if head1 else 0
        val2 = head2.data if head2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current.next = node(total % 10)
        current = current.next

        if head1:
            head1 = head1.next
        if head2:
            head2 = head2.next

    result_list = link_list()
    result_list.head = dummy.next
    return result_list

# print(link_list1.head)
# addrt(link_list1.head,link_list2.head)
temp = add_two_numbers(link_list1.head,link_list2.head)
print("linke 3 travsal start ")
print()
traversal(temp.head)
