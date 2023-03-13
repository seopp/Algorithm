import sys

n = int(input()) # 삼각형의 크기

tri = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)] # 삼각형

d = [0 for _ in range(n+1)] # index층까지의 최대값을 담고 있는 DP테이블

d[1] = tri[0][0]

