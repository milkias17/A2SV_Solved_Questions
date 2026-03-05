import sys

input = sys.stdin.readline


def solve():
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input().strip()))

    row_prefix = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
    col_prefix = [[0 for _ in range(w + 1)] for _ in range(h + 1)]

    for r in range(1, h + 1):
        for c in range(1, w + 1):
            row_connect = 0
            col_connect = 0
            if grid[r - 1][c - 1] == ".":
                if r - 2 >= 0 and grid[r - 2][c - 1] == ".":
                    row_connect += 1
                if c - 2 >= 0 and grid[r - 1][c - 2] == ".":
                    col_connect += 1

            row_prefix[r][c] = (
                row_prefix[r - 1][c]
                + row_prefix[r][c - 1]
                - row_prefix[r - 1][c - 1]
                + row_connect
            )
            col_prefix[r][c] = (
                col_prefix[r - 1][c]
                + col_prefix[r][c - 1]
                - col_prefix[r - 1][c - 1]
                + col_connect
            )

    # print(col_prefix)
    # print(row_prefix)
    q = int(input())
    for _ in range(q):
        ur, lc, br, rc = map(int, input().split())
        total = row_prefix[br][rc]
        total -= row_prefix[ur][rc]
        total -= row_prefix[br][lc - 1]
        total += row_prefix[ur][lc - 1]

        total += col_prefix[br][rc]
        total -= col_prefix[br][lc]
        total -= col_prefix[ur - 1][rc]
        total += col_prefix[ur - 1][lc]

        print(total)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()