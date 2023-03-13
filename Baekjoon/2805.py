n,m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
# trees.sort()
result = 0

while(start<=end):
    mid = (start+end)//2
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree-mid
    if total >= m:
        start = mid + 1
        result = mid
    else:
        end = mid -1

print(result)