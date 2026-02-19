import sys

input = sys.stdin.readline
print = sys.stdout.write


def solve():
    # n = int(input())
    # arr = list(map(int, input().split()))
    matrix = []
    for _ in range(5):
        arr = list(map(int, input().split()))
        matrix.append(arr)

    found = None
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 1:
                found = (i, j)

    count = abs(2 - found[0]) + abs(2 - found[1])
    print(str(count) + "\n")


if __name__ == "__main__":
    solve()

