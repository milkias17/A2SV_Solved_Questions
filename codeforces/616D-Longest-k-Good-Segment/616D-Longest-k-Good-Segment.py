import sys
from collections import Counter

input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    max_len = 0
    max_segment = None
    left = 0
    counter = Counter()

    for right in range(n):
        counter[arr[right]] += 1

        while len(counter) > k:
            counter[arr[left]] -= 1
            if counter[arr[left]] == 0:
                counter.pop(arr[left])
            left += 1

        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_segment = (left + 1, right + 1)

    print(*max_segment)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()