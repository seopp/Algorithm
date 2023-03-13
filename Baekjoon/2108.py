import sys
from collections import Counter

n = int(input())
data = [int(sys.stdin.readline()) for i in range(n)]

print(round(sum(data)/n))
data.sort()
print(data[n//2])
cnt = Counter(data).most_common()

if len(cnt) > 1 and cnt[0][1]==cnt[1][1]: #최빈값 2개 이상
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(max(data)-min(data))