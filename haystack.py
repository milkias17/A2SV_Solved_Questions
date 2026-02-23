from collections import Counter
import sys

input = sys.stdin.readline


def solve():
    # n = int(input())
    # arr = list(map(int, input().split()))
    t = int(input())
    for _ in range(t):
        s = input().strip()
        t = input().strip()

        res = []
        tmp = Counter(s)
        t_list = []
        for char in t:
            if char in tmp and tmp[char] > 0:
                tmp[char] -= 1
            else:
                t_list.append(char)

        t_list.sort()
        for k, v in tmp.items():
            if v > 0:
                print("Impossible")
                break
        else:
            ptr = 0
            holder = 0
            while holder < len(t_list) or ptr < len(s):
                if holder >= len(t_list):
                    res.append(s[ptr])
                    ptr += 1
                elif ptr >= len(s):
                    res.append(t_list[holder])
                    holder += 1
                elif t_list[holder] < s[ptr]:
                    res.append(t_list[holder])
                    holder += 1
                else:
                    res.append(s[ptr])
                    ptr += 1

            print("".join(res))


if __name__ == "__main__":
    solve()
