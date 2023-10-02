"""
https://www.acmicpc.net/problem/2751

Q. 
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

T.
-- 메모리 초과 --
분할 정복 (Devide and Conquer) 기법과 재귀 알고리즘을 이용한 정렬 알고리즘.
pivot 값을 임의로 정하여 값을 기준으로 작은 값들의 그룹, 큰 값들의 그룹으로 나눈다.
return 값으로는 작은 값 그룹, pivot값, 큰 값 그룹을 모두 합치며 작은값/큰값의 재귀함수를 씌워준다.

"""

import sys

# Recursion Error
# Python 이 정한 최대 재귀 깊이보다 재귀가 깊어질 때 발생한다.
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
unsortedArr = []
for i in range(N):
    num = int(sys.stdin.readline())
    unsortedArr.append(num)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    # pivot 값을 기준으로 작은 값, 큰 값을 분할 (임의로 pivot 값을 정함)
    pivot = arr[len(arr)//2]
    lesser, equal, greater = [], [], []
    for i in arr:
        if i < pivot:
            lesser.append(i)
        elif i > pivot:
            greater.append(i)
        else :
            equal.append(i)
    return quick_sort(lesser) + equal + quick_sort(greater)

sorted = quick_sort(unsortedArr)
for i in sorted:
    print(i)