a,b = input().split()

a_reverse = int(a[::-1])
b_reverse = int(b[::-1])

print(max(a_reverse, b_reverse))


