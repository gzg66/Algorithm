"""
题目：
在一个无序数组中，任意相邻的两个数不相等
局部最小定义： arr[i] < arr[i - 1] 并且 arr[i] < arr[i + 1]，则 i 位置局部最小
返回：返回任意一个数组中的局部最小 纸牌屋
""" 
def getLessIndex(arr: list[int]) -> int:
    # 空数组判断
    if arr is None or len(arr) == 0:
        return -1
    
    if len(arr) == 1 or arr[0] < arr[1]:
        return 0
    
    N = len(arr)
    if arr[N-1] < arr[N-2]:
        return N-1
    
    L, R, mid = 0, N-1, 0
    while L <= R:
        mid = ((R - L) >> 1) + L
        if arr[mid] > arr[mid-1]:
            R = mid - 1
        elif arr[mid] > arr[mid+1]:
            L = mid + 1
        else:
            return mid
        

if __name__ == '__main__':
    arr = [9,8,6,5,8]
    print(arr)
    print(getLessIndex(arr))
    
