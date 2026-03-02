import sys

input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())
    paper = input().strip()
    left = 0
    cur_count = 0
    min_count = float("inf")
    for right in range(n):
        if paper[right] == "W":
            cur_count += 1

        if right - left + 1 == k:
            min_count = min(min_count, cur_count)
            if paper[left] == "W":
                cur_count -= 1
            left += 1

    print(min_count)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()

