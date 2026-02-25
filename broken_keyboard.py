import sys

input = sys.stdin.readline


def solve():
    s = input().strip()
    i = 0
    chars = set()
    while i < len(s):
        if i + 1 >= len(s):
            chars.add(s[i])
            i += 1
        elif s[i] == s[i + 1]:
            i += 2
        else:
            chars.add(s[i])
            i += 1

    print("".join(sorted(chars)))


def main():
    sys.setrecursionlimit(200000)
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()

