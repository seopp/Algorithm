import sys

n = int(input())
cnt = n

for i in range(n):
    word = sys.stdin.readline().rstrip("\n")
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)

# 무작정 처음에 리스트로 받으려는 습관 버리자 ,,



