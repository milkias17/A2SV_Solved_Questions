import sys
from collections import Counter

input = sys.stdin.readline


def solve():
    n, l, r = map(int, input().split())
    socks = list(map(int, input().split()))
    left = Counter(socks[:l])
    right = Counter(socks[l:])
    # print(f"TotaL: {total}, left: {left}, right: {right}")
    count = 0

    for k, v in left.items():
        if k in right and right[k] > 0:
            if v >= right[k]:
                left[k] -= right[k]
                right[k] = 0
            else:
                right[k] -= v
                left[k] = 0

    l = sum(left.values())
    r = sum(right.values())

    if l < r:
        left, right = right, left
        l, r = r, l

    num_els = (l - r) // 2
    els = left.most_common()
    for k, v in els:
        if num_els == 0:
            break
        if v == 1:
            num_els -= 1
            count += 1
            left[k] -= 1
            right[k] += 1
        else:
            tmp = v // 2
            tmp = min(num_els, tmp)
            count += tmp
            num_els -= tmp
            left[k] -= tmp
            right[k] += tmp

    for k, v in left.items():
        if k in right and right[k] > 0:
            if v >= right[k]:
                left[k] -= right[k]
                right[k] = 0
            else:
                right[k] -= v
                left[k] = 0

    count += sum(left.values())
    print(count)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
