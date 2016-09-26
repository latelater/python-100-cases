# # 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

# # s = 23432
# s = int(input("输入一个五位数："))

# # print(type(s))
# b = []
# x = 0
# j = 0
# a = 10
# while x < 5:
# 	a = s%10
# 	s = int(s/10)
# 	b.append(a)
# 	x += 1
# print(b)
# for i in range(2) :
#  	if b[i] == b[-1-i] :
#  		j += 1
# if j == 2:
# 	print("是回文")
# else :
# 	print("不是回文")
# 23432
s = input("输入一个正整数：")
for x in range(3):
	if s[x] != s[-1-x] :
		break
if x == 2:
	print("是回文")
else:
	print("不是回文")