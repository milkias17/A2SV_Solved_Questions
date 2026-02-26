import sys

input = sys.stdin.readline


def solve():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    left = 0
    count = 0
    cur_sum = 0

    for right in range(n):
        cur_sum += arr[right]
        while cur_sum > s:
            cur_sum -= arr[left]
            left += 1


def main():
    sys.setrecursionlimit(200000)
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
