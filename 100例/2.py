# 题目：企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；      10万内 10%，高于部分7.5%； 
# 20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；	 20万-40万，5%，高于部分3%
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，     60-100  ，1.5%，1%
# 从键盘输入当月利润I，求应发放奖金总数？
# 程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。

i = int(input("输入利润（单位万）金额："))
k = float(0)
print("利润 = ", i, "万")
if i<=10:
	k = i*0.1
	print("奖金 = ", k, "万")
elif i>10 and i<20:
	k = 10*0.1+(i-10)*0.75
	print("奖金 = ", k, "万")
elif i>=20 and i<40:
	k = i*0.05
	print("奖金 = ", k, "万")
elif i>40 and i<60:
	k = 20*0.05+(i-20)*0.03
	print("奖金 = ", k, "万")
elif i>=60 and i<100:
	k = i*0.015
	print("奖金 = ", k, "万")
elif i>=100:
	k = 60*0.015+(i-60)*0.01
	print("奖金 = ", k, "万")
