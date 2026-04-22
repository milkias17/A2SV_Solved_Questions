from collections import deque
import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    mat = []

    for _ in range(n):
        row = list(map(int, list(input().strip())))
        mat.append(row)

    after_adj = {k: [] for k in range(1, n + 1)}
    before_count = {k: 0 for k in range(1, n + 1)}
    for i in range(n):
        for j in range(i):
            if mat[i][j] == 1:
                after_adj[j + 1].append(i + 1)
                before_count[i + 1] += 1

        for j in range(i + 1, n):
            if mat[i][j] != 1:
                after_adj[j + 1].append(i + 1)
                before_count[i + 1] += 1

    queue = deque()
    for k, v in before_count.items():
        if v == 0:
            queue.append(k)

    res = []
    while queue:
        tmp = queue.popleft()
        res.append(tmp)
        for val in after_adj[tmp]:
            before_count[val] -= 1
            if before_count[val] <= 0:
                queue.append(val)

    print(*res)



def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()