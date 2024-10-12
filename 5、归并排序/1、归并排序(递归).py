def merge(arr: list[int], L: int, mid: int, R: int):
    # 定义辅助数组，长度为R - L + 1
    help = [0] * (R - L + 1)

    # 定义双指针进行归并操作
    p1, p2, i = L, mid + 1, 0
    while p1 <= mid and p2 <= R:
        if arr[p1] <= arr[p2]:
            help[i] = arr[p1]
            p1 +=1
        else:
            help[i] = arr[p2]
            p2 += 1
        i += 1

    # 结束循环
    # 1.左部分未遍历结束
    while p1 <= mid:
        help[i] = arr[p1]
        p1 += 1
        i += 1
    # 2.右部分未遍历结束
    while p2 <= R:
        help[i] = arr[p2]
        p2 += 1
        i += 1
    # 将排序后的数组赋值回原数组
    for j in range(len(help)):
        arr[L + j] = help[j]


def process(arr: list[int], L: int, R: int):
    # 递归边界条件，只有一个元素时结束递归
    if L == R:
        return
    
    mid = ((R - L) >> 1) + L
    # 左部分有序
    process(arr, L, mid)
    # 右部分有序
    process(arr, mid+1, R)
    # 归并
    merge(arr, L, mid, R)


# 归并排序递归写法
def mergeSoft01(arr: list[int]):
    # 如果长度小于等于1，不用排序
    if arr is None or len(arr) <= 1:
        return
    
    # 在 0->len-1 上有序
    process(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    arr = [234,2,543,12,4]
    print(arr)
    mergeSoft01(arr)
    print(arr)