import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    a = input().strip()
    b = input().strip()

    can_flip = [False] * n
    diff = 0
    for i, char in enumerate(a):
        diff += 1 if char == "1" else -1

        if diff == 0:
            can_flip[i] = True

    flipped = False
    for i in range(n - 1, -1, -1):
        char = a[i]

        cur = char
        if flipped:
            cur = "1" if char == "0" else "0"

        if cur != b[i]:
            if not can_flip[i]:
                print("NO")
                return
            flipped = not flipped

    print("YES")


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()