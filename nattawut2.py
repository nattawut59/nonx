class CircularQueue:
    def __init__(self, n):
        self.n = n
        self.queue = [None] * n
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        print("ทางเลือกในการดำเนินการ = 1")
        print(f"ตัวเลขที่นำเข้า = {data}")

      
        if (self.rear + 1) % self.n == self.front:
            print("เพิ่มข้อมูลไม่ได้เพราะคิววงกลมเต็ม")
        else:
            if self.front == -1: 
                self.front = 0
            self.rear = (self.rear + 1) % self.n
            self.queue[self.rear] = data

        print("ทางเลือกในการดำเนินการ =")

    def dequeue(self):
        print("ทางเลือกในการดำเนินการ = 2")

        
        if self.front == -1:
            print("ลบข้อมูลไม่ได้เพราะคิววงกลมว่าง")
        else:
            temp = self.queue[self.front]
            print(f"ตัวเลขที่ลบออก = {temp}")
            self.queue[self.front] = None
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.n

        print("ทางเลือกในการดำเนินการ =")

    def show_less_than_150(self):
        print("ทางเลือกในการดำเนินการ = 3")

        if self.front == -1:
            print("แสดงข้อมูลไม่ได้เพราะคิววงกลมว่าง")
        else:
            i = self.front
            found = False
            while True:
              
                if self.queue[i] is not None and self.queue[i] < 150:
                    print(self.queue[i])
                    found = True
                if i == self.rear:
                    break
                i = (i + 1) % self.n
            if not found:
                print("ไม่มีข้อมูลที่น้อยกว่า 150")

        print("ทางเลือกในการดำเนินการ =")


n = int(input('โปรดระบุขนาดของ Circular Queue ที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป = '))
while n < 5:
    n = int(input('โปรดระบุขนาดของ Circular Queue ที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป = '))
queue = CircularQueue(n)
print("\nโปรดระบุทางเลือกในการดำเนินการ")
print("1 เพิ่มข้อมูลตัวเลขจำนวนเต็มในคิววงกลม")
print("2 ลบข้อมูลที่จัดเก็บในคิววงกลม 1 ตัว")
print("3 แสดงตัวเลขจำนวนเต็มที่มีค่าน้อยกว่า 150 ที่จัดเก็บในคิววงกลมทางจอภาพ")
a = int(input("ทางเลือกในการดำเนินการ = "))
while a == 1 or a == 2 or a == 3 :
   
    if a == 1:
         data = int(input("ตัวเลขที่นำเข้า = "))
         queue.enqueue(data)
    elif a == 2:
         queue.dequeue()
    elif a == 3:
         queue.show_less_than_150()
 
