# data = []
# while True:
#     p = sys.stdin.readline().strip()
#     if p == '0':
#         break
#     data.append(p)

# for i in range(len(data)):
#     if list(data[i]) == list(reversed(data[i])):
#         print("yes")
#     else:
#         print("no")
    
import sys

while True:
    p = sys.stdin.readline().strip()
    if p == '0':
        break
    if p == p[::-1]:
        print('yes')
    else:
        print('no')

