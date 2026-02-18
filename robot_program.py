import sys

input = sys.stdin.readline


def solve():
    t = int(input())

    for _ in range(t):
        n, x, k = list(map(int, input().split()))
        s = input().strip()
        count = 0
        right = None
        found_first = -1

        for count in range(min(n, k)):
            if s[count] == "L":
                x -= 1
            elif s[count] == "R":
                x += 1

            if x == 0:
                found_first = count + 1
                break

        if found_first == -1:
            print(0)
            continue

        ans = 1
        k -= found_first
        x = 0

        for i in range(min(n, k)):
            char = s[i]
            if char == "L":
                x -= 1
            elif char == "R":
                x += 1

            if x == 0:
                right = i + 1
                break

        if right is not None:
            ans += (k // right)

        print(ans)


if __name__ == "__main__":
    solve()

