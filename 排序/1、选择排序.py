from typing import List


def swap(arr: List[int], b: int, a: int):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def selectSoft(arr: List[int]):
    # 判断为空
    if arr is None or len(arr) == 0 or len(arr) == 1:
        return

    # i： 0 - N
    for i in range(len(arr)):
        # j： i - N
        min_index = i
        for j in range(i, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        swap(arr, min_index, i)


if __name__ == '__main__':
    arr = [2, 1, 3, 5, 4]
    print(arr)
    selectSoft(arr)
    print(arr)
