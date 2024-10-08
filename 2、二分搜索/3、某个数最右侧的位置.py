# 判断一个有序数组中<=某个数最右边的位置
def nearestIndex(arr: list[int], value: int) -> int:
    # 初始条件判断
    # arr 未定义或为空， 直接返回-1
    if arr is None or len(arr) == 0:
        return -1
    
    # 定义搜索边界L、R
    L, R, mid = 0, len(arr) - 1, 0
    index = -1

    while L <= R:
        mid = ((R - L) >> 1) + L
        if arr[mid] <= value:
            # <=，证明左边范围都 <= value，则只需要在右边范围继续搜索即可
            index = mid
            L = mid + 1
        else:
            R = mid - 1

    return index

if __name__ == '__main__':
    arr = [1, 3, 3, 3, 5]
    print(arr)
    print(nearestIndex(arr, 3))