import sys


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        a_els = {val: idx for idx, val in enumerate(a)}
        b_els = {val: idx for idx, val in enumerate(b)}
        ops = []
        idx = None

        for i in range(1, ((2 * n) // 2) + 1):
            if i in b_els:
                b_idx = b_els[i]
                while b_idx < i - 1:
                    ops.append([2, b_idx + 1])
                    b_els[b[b_idx]] += 1
                    b_els[b[b_idx + 1]] -= 1
                    b[b_idx], b[b_idx + 1] = b[b_idx + 1], b[b_idx]
                    b_idx += 1

                ops.append([3, b_idx + 1])
                idx = b_idx
                a[idx], b[idx] = b[idx], a[idx]
                del b_els[i]
                a_els[i] = idx
                b_els[b[idx]] = idx

            idx = a_els[i]
            while idx != i - 1:
                ops.append([1, idx])
                a_els[a[idx]] -= 1
                a_els[a[idx - 1]] += 1
                a[idx], a[idx - 1] = a[idx - 1], a[idx]
                idx -= 1

        for i in range(n):
            for j in range(0, n - i - 1):
                if b[j] > b[j + 1]:
                    ops.append([2, j + 1])
                    b[j], b[j + 1] = b[j + 1], b[j]

        print(len(ops))
        if len(ops) > 0:
            for i, j in ops:
                print(f"{i} {j}")


if __name__ == "__main__":
    solve()
