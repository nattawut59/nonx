class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None
        
    def insert(self, data):
        self.data = data
        
        print(f"โปรดป้อนหมายเลขของโหนด Left child ของ {self.data} (ถ้าไม่มีให้ป้อนจำนวนเต็มที่มีค่าน้อยกว่าหรือเท่ากับ 0) : ", end="")
        left_data = int(input())
        if left_data > 0:
            self.leftChild = Node()
            self.leftChild.insert(left_data)
        
        print(f"โปรดป้อนหมายเลขของโหนด Right child ของ {self.data} (ถ้าไม่มีให้ป้อนจำนวนเต็มที่มีค่าน้อยกว่าหรือเท่ากับ 0) : ", end="")
        right_data = int(input())
        if right_data > 0:
            self.rightChild = Node()
            self.rightChild.insert(right_data)

    def PreOrder(self,tree):
        if tree :
            print(tree.data, end=" ")
            self. PreOrder(tree.leftChild)
            self.PreOrder(tree.rightChild)

    def InOrder(self,tree):
        if tree :
            self.InOrder(tree.leftChild)
            if tree.data > 150:  
                print(tree.data, end=" ")
            self.InOrder(tree.rightChild)

    def PostOrder(self,tree):
        if tree:
            self.PostOrder(tree.leftChild)
            self.PostOrder(tree.rightChild)
            if tree.data % 7 == 0:  
                print(tree.data, end=" ")


root = Node()
print("โปรดป้อนจำนวนเต็มเพื่อจัดเก็บที่ Root node : ", end="")
root_value = int(input())
root.insert(root_value)

print("\nทางเลือกในการดำเนินการ")
print("1. ท่องไปในต้นไม้ทวิภาคแบบ Pre-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่เป็นเลขคู่ทางจอภาพ")
print("2. ท่องไปในต้นไม้ทวิภาคแบบ In-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่มีค่าน้อยกว่า 150 ทางจอภาพ")
print("3. ท่องไปในต้นไม้ทวิภาคแบบ Post-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่หารด้วย 7 ลงตัวทางจอภาพ")

choice = input("ทางเลือกในการดำเนินการ: ")

if choice == "1":
    print("Pre-order = ", end="")
    PreOrder(tree)  
elif choice == "2":
    print("In-order = ", end="")
    InOrder(tree)   
elif choice == "3":
    print("Post-order = ", end="")
    PostOrder(tree) 
