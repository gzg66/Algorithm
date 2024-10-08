def findKTimes(arr: list[int], k: int, m: int) -> int:
    rest = [0] * 32

    for num in arr:
        for i in range(32):
            rest[i] += ((num >> i) & 1)
            
    res = 0
    for i in range(32):
        if rest[i] % m != 0:
            res |= (1 << i)

    return res

if __name__ == '__main__':
    arr = [1,1,1,2,2,2,99,99]
    print(findKTimes(arr, 2, 3))