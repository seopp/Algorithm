# s = input()
# answer = []

# for i in range(ord('a'),ord('z')+1):
#     if chr(i) in s:
#         answer.append(s.find(chr(i)))
#     else:
#         answer.append(-1)

# print(' '.join(map(str,answer)))

s = input()
for i in range(97,123):
    print(s.find(chr(i)), end=' ') # find 함수는 해당 문자가 없으면 -1을 리턴
