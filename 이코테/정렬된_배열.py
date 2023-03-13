n,x = map(int, input().split())
num_list = list(map(int, input().split()))
# print(num_list.count(x))
# 이렇게 짜면 시간복잡도가 O(n)이라서 시간 초과 !! 이진탐색으로 풀어서 시간복잡도를 O(logN)으로 만들어야함

from bisect import bisect_left,bisect_right

def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index - left_index

count = count_by_range(num_list,x,x)

if count ==0:
    print(-1)
else:
    print(count)

