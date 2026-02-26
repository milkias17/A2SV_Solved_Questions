import sys

input = sys.stdin.readline


def solve():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    left = 0
    cur_sum = 0
    max_len = float("inf")

    for right in range(n):
        cur_sum += arr[right]
        while cur_sum >= s:
            max_len = min(max_len, right - left + 1)
            cur_sum -= arr[left]
            left += 1

    print(max_len if max_len != float("inf") else -1)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
