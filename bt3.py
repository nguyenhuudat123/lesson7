# thêm chuỗi s vào mỗi phần tử trong list cũ để tạo ra list mới
lst_1 = ['as', 'g', 45]
s = 'strx'
lst_2 =[]
for item in lst_1:
	 lst_2.append(str(item) + s)
print(lst_2)