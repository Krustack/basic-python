#การแสดงค่าในlist
fruits = ["apple","banana", "cherry","watermelon","blueberry"]
fruits.append("orange")
fruits.insert(3,"grape")
tropical = ["mango", "pineapple", "papaya"]
fruits.extend(tropical)
#ลบค่าในlist
fruits.remove("watermelon")
fruits.pop(1)
#del fruits
fruits.sort(reverse=True)
print(fruits)
#ชื่อ.......สกุล.......ชั้น....เลขที่.....