# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
# 程序分析：学会分解出每一位数。\

s = input("输入一个正整数：")
while len(s) > 5:
	s = input("请从新输入！")
	print("\n")
print("长度为：", len(s))
print('逆序输出：')
for i in range(len(s)):
	print(s[-1-i], ' ', end = '')
	