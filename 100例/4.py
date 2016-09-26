# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊 　　　　　　情况，闰年且输入月份大于3时需考虑多加一天：
year = int(input('输入年：'))
month = int(input('输入月：'))
day = int(input('输入天：'))
count = 0
monthday = [31,28,31,30,31,30,31,31,30,31,30,31]
i = month - 1
# month1 = [31,29,31,30,31,30,31,31,30,31,30,31]
if year%4 == 0 and year%100 != 0:
	for x in monthday(0,i):
		print(x)
		# count+ = x
	if month>2:
		count = count + day +1
	else:
		count = count + day
	print(month,"月",day,"天是",year,"年的第",count,"天")
else:
	for x in monthday(0,i):
		# count+ = x
		count = count + day
	print(month,"月",day,"天是",year,"年的第",count,"天")

