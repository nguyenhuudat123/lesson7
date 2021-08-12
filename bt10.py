# loại bỏ phần tử trùng lặp
lst_a = [1,2,3,42,32,32,22,344,22112,2,233321,2233,12,33,2,2,11,2,3,12,3,23345,53,2,1,13,344,4]
lst_b = [lst_a[0]]
for item in lst_a:
	if item not in lst_b:
		lst_b.append(item)
print(lst_b)


# nếu dùng sao chép chuõi sẵn rồi xóa thì khi duyệt các phânf tử trong i sẽ có thể out idex do k cập nhật ki