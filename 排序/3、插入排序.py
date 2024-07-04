from typing import List


def swap(arr: List[int], b: int, a: int):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def charuSoft(arr: List[int]):
    # 判断为空
    if arr is None or len(arr) == 0 or len(arr) == 1:
        return

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] >= arr[j - 1]:
                break
            swap(arr, j, j - 1)


if __name__ == '__main__':
    arr = [2, 1, 3, 1, 4, -5]
    print(arr)
    charuSoft(arr)
    print(arr)
