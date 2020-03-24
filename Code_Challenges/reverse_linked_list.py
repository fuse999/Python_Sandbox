
# How do you reverse a singly linked list without recursion? 
# You may not store the list, or it’s values, in another data structure.



# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, storage):  
        self.storage = storage  
        self.next = None 
  

class LinkedList: 
  

    def __init__(self): 
        self.head = None


    def push(self, new_storage): 
        new_node = Node(new_storage) 
        new_node.next = self.head 
        self.head = new_node 

    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 

    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.storage, 
            temp = temp.next)


list1 = LinkedList() 
list1.push(6)
list1.push(5) 
list1.push(23) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printList()
list1.reverse_list()
list1.printList()