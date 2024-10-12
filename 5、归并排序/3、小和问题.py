import math


def merge(arr, L, mid, R):
    help = [0] * (R - L + 1)
    sum, p1, p2, i = 0, L, mid + 1, 0
    while p1 <= mid and p2 <= R:
        if arr[p1] < arr[p2]:
            # 拷贝左数累加
            # 拷贝左边数的时候，右边数还有(R - p2 + 1 )个比它大
            sum += arr[p1] * (R - p2 + 1 )
            help[i] = arr[p1]
            p1 += 1
        else:
            help[i] = arr[p2]
            p2 += 1
        i += 1
    
    while p1 <= mid:
        help[i] = arr[p1]
        p1 += 1
        i += 1
    while p2 <= R:
        help[i] = arr[p2]
        p2 += 1
        i += 1
    for j in range(len(help)):
        arr[j + L] = help[j]

    return sum


def process(arr, L, R):
    if L == R:
        return 0
    
    mid = ((R - L) >> 1) + L
    s1 = process(arr, L, mid)
    s2 = process(arr, mid + 1, R)
    s3 = merge(arr, L, mid, R)
    return s1 + s2 + s3


def smallSum(arr: list[int]) -> int:
    if arr is None or len(arr) <= 1:
        return 0
    
    return process(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    arr = [6,6]
    print(arr)
    print(smallSum(arr))