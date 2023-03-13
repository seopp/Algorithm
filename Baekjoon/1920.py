n = int(input()) # a의 길이
a = set(map(int,input().split()))
m = int(input()) # b의 길이
b = list(map(int,input().split()))

for i in b:
    print(1) if i in a else print(0)