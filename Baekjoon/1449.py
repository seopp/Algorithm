n,l = map(int, input().split())
water = list(map(int, input().split()))
count = 0    # 테이프 갯수
water.sort() # 오름차순 정렬
iscount =[True] * len(water) # True이면 아직 막지 않은곳, False이면 막은 곳

for i in range(len(water)): 
    if iscount[i] == True: # 막지 않은 곳이면
        count+=1 # 테이프 한개 추가
        iscount[i] = False # 막은 곳으로 변경
        for j in range(len(water)-i-1,0,-1): # 현재 위치를 기점으로 가장 먼곳부터 탐색
            if water[i+j]-water[i]+1 <= l:   # 여러 개를 한번에 막을 수 있으면
                for k in range(0,j+1):       
                    iscount[i+k] = False     # 현재 위치 ~ 한번에 막을 수 있는 위치까지를 False로 변경
                break                        # 이후 더 탐색하지 않고 for문 종료
print(count)