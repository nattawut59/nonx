
def is_empty(mystack):
    return len(mystack) == 0
def is_full(mystack, size):
    return len(mystack) >= size
def push(mystack, size):
    if is_full(mystack, size):
        print("Stack เต็ม ไม่สามารถเพิ่มข้อมูลได้")
    else:
        value = float(input("ป้อนค่าทศนิยมเพื่อเพิ่มลงใน Stack: "))
        stack.append(value)
        print("เพิ่มข้อมูลเรียบร้อยแล้ว")
def pop(stack):
    if is_empty(mystack):
        print("Stack ว่าง ไม่มีข้อมูลให้ลบ")
    else:
        removed_value = stack.pop()
        print(f"ลบข้อมูล {removed_value} ออกจาก Stack")
def display(mystack):
    if is_empty(stack):
        print("Stack ว่าง")
    else:
        print("ข้อมูลทั้งหมดใน Stack:", stack)
def average(mystack):
    if is_empty(mystack):
        print("Stack ว่าง ไม่สามารถคำนวณค่าเฉลี่ยได้")
    else:
        avg = sum(mystack) / len(stack)
        print(f"ค่าเฉลี่ยของข้อมูลใน Stack คือ: {avg}")




n = int(input('โปรดระบุขนาดของ stack ที่มีขนาดตั้งแต่6ช่องขึ้นไป = '))
while n <6:
    n = int(input('โปรดระบุขนาดของ stack ที่มีขนาดตั้งแต่6ช่องขึ้นไป = '))
mystack = []*n
print("\nเลือกการทำงาน:")
print("1: เพิ่มข้อมูลใน Stack")
print("2: ลบข้อมูลจาก Stack")
print("3: แสดงข้อมูลทั้งหมดใน Stack")
print("4: แสดงค่าเฉลี่ยของข้อมูลใน Stack")
a=int(input("ป้อนหมายเลขตัวเลือก: "))
while a ==1 or a == 2 or a== 3 or a==4 :
    if a == 1:
        push(mystack, size)
    elif a == 2:
        pop(mystack)
    elif a == 3:
        display(mystack)
    elif a == 4:
        average(mystack)



















































