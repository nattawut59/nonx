class Node:
    def __init__(self, info = None):
        self.info = info
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def AtTheBegining(self, data):
        if self.head != None:
            NewNode = Node(data)
            NewNode.next = self.head
            self.head = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode
    
    def AtTheEnd(self, data):
        if self.head == None:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.tail.next = NewNode
            self.tail = NewNode
    
    def display(self):
        current = self.head
        print("\nข้อมูลใน Singly linked list คือ:")
        while current:
            print(current.info)
            current = current.next
        print(f"ข้อมูลที่เก็บในตำแหน่งที่พอยน์เตอร์ head นี้ คือ {self.head.info if self.head else None}")
        print(f"ข้อมูลที่เก็บในตำแหน่งที่พอยน์เตอร์ tail นี้ คือ {self.tail.info if self.tail else None}")
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(f"จำนวนของข้อมูลที่เก็บใน Singly linked list คือ {float(count):.2f}")

list = SLinkedList()
print("\nการเลือกในการดำเนินการกับ Singly linked list")
print("B : เพิ่มข้อมูลที่จุดเริ่มต้นของ Singly linked list")
print("E : เพิ่มข้อมูลแบบต่อจากโหนดสุดท้ายของ Singly linked list")    
choice = input("การเลือกในการดำเนินการ = ")
while  choice in ( 'B' ,'E' ):
    
   if choice == 'B':
        data = int(input("ตัวเลขที่ต้องการเพิ่ม คือ "))
        list.AtTheBegining(data)

   elif choice == 'E':
        data = int(input("ตัวเลขที่ต้องการเพิ่ม คือ "))
        list.AtTheEnd(data)
   choice = input("การเลือกในการดำเนินการ = ")        
list.display()

