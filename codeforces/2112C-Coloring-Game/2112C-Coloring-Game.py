import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    count = 0

    for i in range(2, n):
        left = 0
        right = i - 1

        while left < right:
            if arr[left] + arr[right] + arr[i] <= arr[-1]:
                left += 1
                continue

            if arr[left] + arr[right] > arr[i]:
                count += right - left
                right -= 1
            else:
                left += 1

    print(count)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()