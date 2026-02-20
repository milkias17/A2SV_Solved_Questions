import sys

input = sys.stdin.readline
print = sys.stdout.write


def solve():
    # n = int(input())
    # arr = list(map(int, input().split()))
    t = int(input())

    for _ in range(t):
        n, k = list(map(int, input().split()))
        arr = []
        for _ in range(n):
            arr.append(list(map(int, input().split())))

        arr.sort(key=lambda x: (x[0], x[1], -x[2]))
        for casino in arr:
            if k < casino[0]:
                break
            if casino[2] > k:
                k = casino[2]

        print(str(k) + "\n")


if __name__ == "__main__":
    solve()

