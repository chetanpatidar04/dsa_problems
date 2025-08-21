# Stack Operations
# push(): Insert a new element into the stack (i.e just insert a new element at the beginning of the linked list.)
# pop(): Return the top element of the Stack (i.e simply delete the first element from the linked list.)
# peek(): Return the top element.
# display(): Print all elements in Stack.


class node():
    def __init__(self,data):
        self.data = data
        self.next = None


class linked_list():
    def __init__(self):
        self.head = None
    
    def push(self,data):
        if self.head is None:
            self.head = node(data)
            return           
        current = self.head
        while(current.next):
            current = current.next
        current.next = node(data)

    def display(self):
        if self.head is None:
            print("No element in the list")
            return
        current = self.head
        while(current.next):
            print(str(current.data) +" ==> ", end="")
            current = current.next
        print(current.data)

    def pop(self):
        if self.head is None:
            print("No data in list")
            return
        if self.head.next == None:
            self.head = None  
            return
        
        current = self.head
        while(current.next):
            prev = current
            current = current.next
    
        current = prev
        current.next = None
        del prev


    def peek(self):
        if self.head is None:
            print("No element in the list")
            return
        current = self.head
        while(current.next):
            current = current.next
        print(current.data)


linked_list = linked_list()
linked_list.push(10)
linked_list.push(20)
linked_list.push(30)
linked_list.push(40)
linked_list.pop()
linked_list.display()
linked_list.peek()