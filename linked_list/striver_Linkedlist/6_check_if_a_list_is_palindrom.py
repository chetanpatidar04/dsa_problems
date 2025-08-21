# class node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class linked_list():
#     def __init__(self):
#         self.head = None
    
#     def insert_data(self,data):
#         if self.head is None:
#             self.head = node(data)
#             return        
#         current = self.head
#         while(current.next):
#             current = current.next
#         current.next = node(data)
    

#     def travesal(self):
#         if self.head is None:
#             print("No element present in linked list")
#             return None
#         if self.head.next is None:
#             return self.head
#         current = self.head        
#         while(current):
#             print(str(current.data) + " " ,end= "")
#             current = current.next

# # ======================================= brute force with stack ========================================= 

#     def check_palindrom(self):
#         if self.head is None:
#             print("No elements in the list")
#             return None
#         if self.head.next is None:
#             print("list is a valid palindrom with one node ")
#             return self.head
#         st = []
#         current = self.head
#         while(current):
#             st.append(current.data)
#             current = current.next
        
#         current1 = self.head
#         while(current1):
#             value = st.pop()
#             print(value,current1.data)
#             if value != current1.data:
#                 print("list is not a valid palindrom")
#                 return self.head
#             current1 = current1.next
#         print("list is a valid palindrom")
#         return self.head        

# # ======================================= Optimal solution ========================================= 
#     def check_palindrom_optimal_sol(self):
#         if self.head is None:


# linked_list = linked_list()
# linked_list.insert_data(10)
# # linked_list.insert_data(20)
# # linked_list.insert_data(30)
# # linked_list.insert_data(20)
# # linked_list.insert_data(10)
# linked_list.travesal()
# linked_list.check_palindrom()
# linked_list.travesal()