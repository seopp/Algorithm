import sys
data =[int(sys.stdin.readline()) for _ in range(10)]
n = set()
for i in data:
    n.add(i%42)
print(len(n))
