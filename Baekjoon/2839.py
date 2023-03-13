n = int(input()) # 설탕

count = 0 # 봉지 수
while n>=0: 
    if n%5==0:# n이 5의 배수이면
        count += (n//5) #5로 나눈 몫을 더함
        print(count)
        break
    n -= 3 # 5의 배수가 될 때까지 3씩 빼줌
    count += 1 # 봉지 수 추가
else:
    print(-1) # while문에서 5의 배수를 만족하지 못하고 n이 음수가 되어 빠져 나오면 while ~ else 문을 통해 -1을 출력