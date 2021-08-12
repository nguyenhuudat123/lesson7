# tìm min, max trong x
lst = [1,3,4,6789,4,-3,6]
min_ = lst[0]
max_ = lst[1]

max_ = max(lst)
print('max = ', max_)

for item in lst:
	if item <= min_:
		min_ = item
print('min = ', min_)

