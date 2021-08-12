lst_1 = [[1,2,4], [3,4,3], [1,2,3]]
lst_2 = [[1,3,3], [3,5,4], [2,3,3]]
lst_3 = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(0,3):
	for j in range(0,3):
		for m in range(0, 3):
			lst_3[i][j] = lst_1[i][m] * lst_2[m][j] 
	print(lst_3[i])





