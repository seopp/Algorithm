import sys

t = int(input())

for _ in range(t):
    n = int(sys.stdin.readline())
    d = [[0 for _ in range(2)] for _ in range(n+1)]  # index까지의 0과 1의 개수를 담고 있는 DP 테이블
    d[0] = [1,0]
    if n >=1:
        d[1] = [0,1]
    if n >=2:
        for i in range(2,n+1):
            d[i][0] = d[i-1][0] + d[i-2][0]
            d[i][1] = d[i-1][1] + d[i-2][1]
    print(d[n][0],d[n][1])
    print(d[n])
