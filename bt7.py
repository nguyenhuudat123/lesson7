# kiểm tra 2 list cos phần tử chung hay không.
lst_1 = [234,34,34,56,7,8,8,8,6,5,5,4343,34,4,4,5]
lst_2 = ['adsf', "sd", ['asdf',1,2,3],34,3,4,34,4,5,6,7,33,4,4,5,55,4]
count_ = 0
for item in lst_1:
	if item in lst_2:
 		count_ += 1
print('2 list có phần tử chung') if count_ != 0 else print('2 list không có phần tử chung')