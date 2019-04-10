# class Node():
#     def __init__(self, data=None):
#         self.__data = data
#         self.__link = None
#     @property
#     def data(self):
#         return self.__data 

#     @data.setter
#     def data(self, data):
#         self.__data = data

    
#     @property
#     def link(self):
#         return self.__link

#     @link.setter
#     def link(self, link):
#         self.__link = link


# class SingleLinkedList():

#     def __init__(self, data):
#         self.__head = None
#         self.__size = 0
#     @property 
#     def head(self):
#         return self.__head

#     @head.setter
#     def head(self, link):
#         self.__head = link 

#     @property
#     def size(self):
#         return self.__size

#     @size.setter
#     def size(self, data):
#         self.__size += data
   
#     def empty(self):
#         if self.__size == 0:
#             return True 
#         else:
#             return False

#     def li_size(self):
#         return self.__size

#     def add(self, data):
#         new_node = Node()
#         new_node.link = self.head
#         self.head = new_node
#         self.size += 1

#     def search(self, target):
#         temp = self.head
#         while temp:
#             if temp.data == target:
#                 return temp
#             else:
#                 temp = temp.link
#         return None
    
#     def delete(self):
#         if self.head == None:
#             return
#         else:
#             self.head = self.head.link




# if __name__ == "__main__":
#     sll = SingleLinkedList()
#     sll.add(1)
#     sll.add(3)
#     sll.add(5)
#     sll.add(7)
#     sll.add(10)

#     print(f"리스트의 갯수 ; {sll.size()} ")

#     sll.delete()
#     sll.delete()
#     sll.search(5)
#     print("*"*100)
    