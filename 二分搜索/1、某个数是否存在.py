def exist(arr: list[int], num: int) -> bool:
    # 初始条件判断
    # arr 未定义或为空， 直接返回False
    if arr is None or len(arr) == 0:
        return False
    
    # 定义搜索边界L、R
    L, R, mid = 0, len(arr) - 1, 0
    
    # 二分边界
    while L < R:
        mid = ((R - L) >> 1) + L
        if arr[mid] == num:
            return True
        elif arr[mid] < num:
            # 左边范围没有，直接删除，L = mid + 1
            L = mid + 1
        else:
            # 右边范围没有，直接删除，R = mid - 1
            R = mid - 1

    # 二分到底后，此时L = R
    # 判断当前位置是否相等即可
    return arr[L] == num
    

if __name__ == '__main__':
    arr = [1, 3, 5]
    print(arr)
    print(exist(arr, 3))