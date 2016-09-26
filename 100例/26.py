# 题目：利用递归方法求5!。
# 程序分析：递归公式：fn=fn_1*4!

x = 1
i = 1
def fn(i, x):
	if i > 5:
		print(x)
		return
	x *= i
	fn(i+1, x)
fn(x, i)