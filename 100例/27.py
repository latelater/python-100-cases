# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

i = 4
x = input("输入五个字符：")
def fanxu(i,x):
	if i < 0:
		return
	print(x[i])
	fanxu(i-1, x)
fanxu(i,x)