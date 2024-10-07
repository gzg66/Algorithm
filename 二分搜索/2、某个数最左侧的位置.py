# 判断一个有序数组中>=某个数最左边的位置
def nearestIndex(arr: list[int], value: int) -> int:
    # 初始条件判断
    # arr 未定义或为空， 直接返回-1
    if arr is None or len(arr) == 0:
        return -1
    
    # 定义搜索边界L、R
    L, R, mid = 0, len(arr) - 1, 0
    index = -1
    
    # 此时使用 <= 保证当前边界内至少存在一个数字
    # 原因： 因为要比较当前边界内的数字与 value 大小情况
    # 若没有数字，则不知道当前边界如何变化
    while L <= R:
        mid = ((R - L) >> 1) + L
        if arr[mid] >= value:
            # >= ，则证明右边范围都 >= value
            # 左边范围可能存在 >= value的数字
            # 所以，R = mid - 1
            # index = mid
            R = mid - 1
            index = mid
        else:
            # <=，则证明左边范围肯定没有符合的数
            # 直接在右边范围进行搜索
            L = mid + 1

    return index

if __name__ == '__main__':
    arr = [1, 3, 3, 3, 5]
    print(arr)
    print(nearestIndex(arr, 3))