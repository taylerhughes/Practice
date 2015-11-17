#Completed on 17/11/2015
i = int(input())
d = input().split()

negative = 0
positive = 0
zero = 0

for x in range(0, i):
	if int(d[x]) < 0:
		negative += 1
	elif int(d[x]) > 0:
		positive += 1
	else:
		zero += 1

print(round(positive / i, 6))
print(round(negative / i, 6))
print(round(zero / i, 6))