import sys
from collections import Counter

input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    counter = Counter()
    left = 0
    count = 0

    for right in range(n):
        counter[arr[right]] += 1
        while len(counter) > k:
            counter[arr[left]] -= 1
            if counter[arr[left]] == 0:
                del counter[arr[left]]

            left += 1
        count += right - left + 1

    print(count)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()

