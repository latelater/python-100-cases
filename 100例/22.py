# 题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

# import itertools
# l = {'a':'', 'b':'', 'c':''}
# ll = ['x', 'y', 'z']
# lll = ['a', 'b', 'c']
# for i in range(0,3):
# 	for j in lll:
# 		l[j] = ll[i]
# 		if l['a'] != 'x':
# 			if l['c'] != 'x' and l['c'] != 'z' :
# 				print(l)



# itertools.permutations([1,2,3,4],2)