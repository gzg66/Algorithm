def merge(arr, L, mid, R):
    help = [0] * (R - L + 1)
    p1, p2, i = L, mid + 1, 0
    while p1 <= mid and p2 <= R:
        if arr[p1] <= arr[p2]:
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

# 归并排序非递归
def mergeSoft01(arr: list[int]):
    # 数组为空或长度小于等于1，不用排序
    if arr is None or len(arr) <= 1:
        return 
    
    # 归并排序步长
    step = 1
    while step <= len(arr):
        # 归并排序最左的位置
        L = 0
        # 相邻两个步长的两个子数组 merge
        while L < len(arr):
            M = L + step - 1
            if M >= len(arr):
                break
            R = min(len(arr) - 1, M + step)
            merge(arr, L, M, R)
            L += (step * 2)

        # 防溢出
        if step > len(arr) / 2:
            break
        # 步长 × 2
        step <<= 1

    return


if __name__ == '__main__':
    arr = [234,2,543,12,4]
    print(arr)
    mergeSoft01(arr)
    print(arr)