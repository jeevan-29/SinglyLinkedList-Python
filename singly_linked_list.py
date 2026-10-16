class Node:
def init(self, data):
self.data = data
self.next = None

class SinglyLinkedList:
def init(self):
self.head = None

def add_first(self, data):  
    new = Node(data)  
    new.next = self.head  
    self.head = new  

def add_last(self, data):  
    new = Node(data)  
    if self.head is None:  
        self.head = new  
        return  

    temp = self.head  
    while temp.next:  
        temp = temp.next  
    temp.next = new  

def add_between(self, data, index):  
    temp = self.head  
    for i in range(index - 1):  
        temp = temp.next  

    new = Node(data)  
    new.next = temp.next  
    temp.next = new  

def remove_first(self):  
    if self.head:  
        self.head = self.head.next  

def remove_last(self):  
    if self.head is None:  
        return  
    if self.head.next is None:  
        self.head = None  
        return  

    temp = self.head  
    while temp.next.next:  
        temp = temp.next  
    temp.next = None  

def remove_between(self, index):  
    temp = self.head  
    for i in range(index - 1):  
        temp = temp.next  
    temp.next = temp.next.next  

def display(self):  
    temp = self.head  
    while temp:  
        print(temp.data, end=" -> ")  
        temp = temp.next  
    print("None")

Main class

class Main:
lst = SinglyLinkedList()

lst.add_first(20)  
lst.add_first(10)  
lst.add_last(30)  
lst.add_between(15, 1)  
lst.display()  

lst.remove_first()  
lst.display()  

lst.remove_last()  
lst.display()  

lst.remove_between(1)  
lst.display()

Main()
