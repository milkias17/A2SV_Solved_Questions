import sys

input = sys.stdin.readline


def solve():
    m = int(input())
    p = list(map(int, input().split()))

    ops = 0

    def merge(left, right):
        nonlocal ops
        new_arr = []

        if left[0] < right[0]:
            new_arr.extend(left)
            new_arr.extend(right)
        else:
            new_arr.extend(right)
            new_arr.extend(left)
            ops += 1

        return new_arr

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

    res = merge_sort(p)
    if not all(res[i] <= res[i + 1] for i in range(len(res) - 1)):
        print(-1)
    else:
        print(ops)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()