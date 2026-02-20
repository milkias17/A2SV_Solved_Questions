import sys

input = sys.stdin.readline
# print = sys.stdout.write


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    prefix_right = [None] * len(arr)
    cur_sum = 0
    for i in range(len(arr) - 1, -1, -1):
        prefix_right[i] = cur_sum
        cur_sum += arr[i]

    prefix_left = []
    cur_sum = 0
    for i in range(0, len(arr)):
        prefix_left.append(cur_sum)
        cur_sum += arr[i]

    min_idx = 0
    min_val = float("inf")
    for i, num in enumerate(arr):
        left_sum = prefix_left[i]
        right_sum = prefix_right[i]
        right_count = len(arr) - 1 - i

        left_sum = (i * num) - left_sum
        right_sum -= right_count * num

        if left_sum + right_sum < min_val:
            min_val = left_sum + right_sum
            min_idx = i

    print(arr[min_idx])


if __name__ == "__main__":
    solve()
