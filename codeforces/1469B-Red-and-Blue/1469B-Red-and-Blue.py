import sys

input = sys.stdin.readline


def get_prefix(arr):
    n = len(arr)

    prefix = [None] * n
    cur_sum = 0
    right = n - 1
    for left in range(n - 1, -1, -1):
        if cur_sum < 0:
            cur_sum = arr[left]
            right = left
        else:
            cur_sum += arr[left]

        prefix[left] = (cur_sum, left, right)

    return prefix


def solve():
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    prefix_r = get_prefix(r)
    prefix_b = get_prefix(b)

    i = 0
    j = 0
    arr = []
    while i < n or j < m:
        if i >= n or (j < m and prefix_b[j] > prefix_r[i]):
            _, left, right = prefix_b[j]
            for idx in range(left, right + 1):
                arr.append(b[idx])
            j = right + 1
        elif j >= m or prefix_r[i] >= prefix_b[j]:
            _, left, right = prefix_r[i]
            for idx in range(left, right + 1):
                arr.append(r[idx])
            i = right + 1

    max_sum = float("-inf")
    cur_sum = 0
    for num in arr:
        cur_sum += num
        max_sum = max(max_sum, cur_sum)

    print(max(0, max_sum))


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()