import sys
from collections import Counter

input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0

    counter_a = Counter(a)
    counter_b = Counter(b)

    for k, v in counter_a.items():
        if k not in counter_b:
            continue
        count += v * counter_b[k]

    print(count)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
