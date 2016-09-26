# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　　　　　
# 程序源代码：  素数筛选法：把所有偶数都标记为false


import math
count = 0
for i in range(1,100):
	x = int(math.sqrt(i))
	for j in range(2,x + 1):
		k = i%j
		if k == 0:
			break
		elif j == x:
			count += 1
			print(i)
print("总数为：", count)
	# # print(i)
 #   for( i=3; i<=sqrt(n); i+=2 )
 #      {   if(prime[i])
 #          for( j=i+i; j<=n; j+=i ) prime[j]=false;
 #      }