#Completed 12/11/2015
i = int(input())
d = []

for x in range(0, i):
	d.append(input().split())

def main_diagonal():
	first = 0
	for y in range(0, i):
		first += int(d[y][y])
	return first

def secondary_diagonal():
	second = 0
	d.reverse()
	for y in range(0, i):
		second += int(d[y][y])
	return second

print(abs(main_diagonal() - secondary_diagonal()))