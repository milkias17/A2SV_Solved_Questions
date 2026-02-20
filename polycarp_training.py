import sys

input = sys.stdin.readline
print = sys.stdout.write


def solve():
    # n = int(input())
    # arr = list(map(int, input().split()))

    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    k = 1
    i = 0
    while k <= n:
        while i < len(arr) and arr[i] < k:
            i += 1

        if i >= len(arr):
            break

        k += 1
        i += 1

    k -= 1
    print(str(k))


if __name__ == "__main__":
    solve()
