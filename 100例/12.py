# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
# 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
# 程序源代码：
# global x
# x = 0
def shuixian(i, x):
	n = i%10
	x += n*n*n
	if i>= 10:
		shuixian(i/10, x)
	return x

for i in range(100,1000):
	x = 0
	j = shuixian(i, x)
	if i == j:
		print(i)
