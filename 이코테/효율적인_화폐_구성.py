import sys
n,k = map(int,input().split())

coins = [int(sys.stdin.readline()) for _ in range(n)]

d = [10001] * (k+1)

d[0] = 0
# 각 코인마다 DP 테이블 갱신
for i in range(n):  # 동전 개수만큼
    for j in range(coins[i], k+1): # 각 동전의 단위부터 만들고자하는 화폐까지
        d[j] = min(d[j], d[j-coins[i]]+1)

if d[k] == 10001: # 만들 수 없으면
    print(-1)
else: 
    print(d[k])