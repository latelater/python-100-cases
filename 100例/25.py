# 题目：求1+2!+3!+...+20!的和。
# 程序分析：此程序只是把累加变成了累乘。

y = 0
x = 1
for i in range(1,21):
	# x = 1
	x *= i
	y += x
print(y)