# add 5 phần tử ngẫu nhiên từ list có sẵn vào list mới.
import random

list_1 = [1,2,3,4,5,6,7,89,6]
list_2 = []
for i in range(5):
	list_2.append(list_1[random.randint(0,len(list_1)-1)])		# nếu để len thì nó sẽ chạy từ 0 đến len, error
print(list_2)

list_3 =[]
for i in range(5):
	list_3.append(random.choice(list_1))
print(list_3)
