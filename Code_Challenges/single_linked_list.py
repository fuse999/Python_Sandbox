# How do you find and return the middle node of a 
# singly linked list in one pass? You do not have
# access to the length of the list. If the list 
# is even, you should return the first of the two
# "middle" nodes. You may not store the nodes in 
# another data structure.


# Plan

# set var for node count
# (incremnt 2 diffrent heads traverse SLL)
# if the list is odd
# set variable for tracking middle node (count/2)
# if the list is even set 2 vars with one offset by -1




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
  
    # Function to get the middle
    def printMiddle(self): 
        sl_scan = self.head 
        fst_scan = self.head 
  
        if self.head is not None: 
            while (fst_scan is not None and fst_scan.next is not None): 
                fst_scan = fst_scan.next.next
                sl_scan = sl_scan.next
            print("The middle element is: ", sl_scan.storage) 


list1 = LinkedList() 
list1.push(6)
list1.push(5) 
list1.push(23) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()