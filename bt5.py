# tìm phần tử xuất hiện nhiều nhất trong chuỗi
lst = [1,2,3,4,5,54,3,2,2,3,4,2,4,'sf','fg']
count_lst =[]
for i in range(len(lst)):
	count_ = 0
	if lst[i] in lst[:i]:
		count_ = 0
	else:
		for j in range(len(lst)):
			if lst[j] == lst[i]:
				count_ += 1
	count_lst.append(count_)
print('phan tu xuat hien nhieu nhat: ', lst[count_lst.index(max(count_lst))])
