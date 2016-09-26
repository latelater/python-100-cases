# 题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
# 程序分析：在10000以内判断，将该数加上100后再开方，加上268后再开方，如果开方后的结果满足如下条件，即是结果。请看具体分析：
import math
import re
for x in range(1,10000):
	i = x+100
	j = x+268
	a = str(math.sqrt(i))
	b = str(math.sqrt(j))
	print(a,b)
	c = "."
	if a.rfind(c) is -1:
		if b.rfidall(c) is -1:
			print(x)