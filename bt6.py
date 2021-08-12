# ㅇ đếm số chuỗi có độ dài lơns hơn 2, đầu cuối giống nhau.
lst = [2,'asdf', 'asdasdasda', 'dferddd', 's', 'sfdfasf']
count_ = 0
for item in lst:
	if type(item) == str and item[0] == item[-1]:
		count_ += 1
print(count_)

# nếu đảo ngược 2 dk trong if sẽ toang vì no sx check số trước, định dạng như thế là số toang.