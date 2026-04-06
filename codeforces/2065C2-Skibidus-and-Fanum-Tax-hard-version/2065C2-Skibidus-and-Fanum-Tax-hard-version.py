import sys

input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()

    prev = float("-inf")
    for num in a:
        left = -1
        right = m

        while left + 1 < right:
            mid = left + (right - left) // 2

            if b[mid] - num >= prev:
                right = mid
            else:
                left = mid

        chosen = float("inf")
        if num >= prev:
            chosen = num

        if right < m and b[right] - num < chosen:
            chosen = b[right] - num

        if chosen == float("inf"):
            print("NO")
            return

        prev = chosen

    print("YES")


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()