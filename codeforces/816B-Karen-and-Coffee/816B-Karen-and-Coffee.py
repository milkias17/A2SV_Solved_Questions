import sys

input = sys.stdin.readline


def solve():
    n, k, q = map(int, input().split())
    recipes = []
    max_r = 0
    for _ in range(n):
        l, r = map(int, input().split())
        max_r = max(max_r, r)
        recipes.append((l, r))

    prefix = [0] * (max_r + 1)
    for l, r in recipes:
        prefix[l] += 1
        if r + 1 < len(prefix):
            prefix[r + 1] -= 1

    cur = 0
    for i in range(len(prefix)):
        cur += prefix[i]
        prefix[i] = cur

    cur = 0
    for i in range(len(prefix)):
        if prefix[i] >= k:
            cur += 1
        prefix[i] = cur

    for _ in range(q):
        a, b = map(int, input().split())
        count = prefix[min(b, len(prefix) - 1)] - prefix[min(a - 1, len(prefix) - 1)]
        print(count)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()