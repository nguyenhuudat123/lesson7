# chia list thành 2 phần với 1 só nhập vào từ bàn phím

lst_1 = [23, '23', [34,567,8], 2345,6784]
spl = int(input('nhap so phan tu cua list thu 1 muon co: spl = '))
lst_2 = lst_1[0: spl]
lst_3 = lst_1[spl: len(lst_1)]
print(lst_2)
print(lst_3)