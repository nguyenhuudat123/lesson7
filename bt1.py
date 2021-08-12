#  tính tổng, tích các phần tử tỏng list
lst = [34,234,456,67,34,3]
sum_ = 0
product_ = 1
for item in lst:
	sum_ += item
	product_ *= item
print(f"tong : {sum_}, tich: {product_}")
