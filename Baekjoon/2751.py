import sys
n = int(input())

data = [int(sys.stdin.readline()) for _ in range(n)]

data.sort()
[print(data[i]) for i in range(n)]