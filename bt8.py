# đếm các tập có a[i] > a[j] với i<j
lst = [1,2,3,4,43,23,3,4,2,2,34,5,5,6,43,2,3]
count_ = 0
for i in range(len(lst)):
	for j in range(i+1, len(lst)):
			if lst[i] > lst[j]:
				count_ += 1
print(count_)