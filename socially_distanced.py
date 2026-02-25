import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    new_seq = [arr[0]]
    for i in range(1, len(arr) - 1):
        prev = arr[i - 1]
        cur = arr[i]
        next = arr[i + 1]
        if prev <= cur <= next or prev >= cur >= next:
            continue

        new_seq.append(cur)

    new_seq.append(arr[-1])

    print(len(new_seq))
    print(*new_seq)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
