n = int(input())
score = list(map(int, input().split()))

answer = [s/max(score)*100 for s in score]

print(sum(answer)/len(answer))