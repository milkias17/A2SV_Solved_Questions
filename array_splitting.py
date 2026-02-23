def solve():
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    cost = arr[-1] - arr[0]
    tmp = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
    tmp.sort(reverse=True)

    for i in range(k - 1):
        cost -= tmp[i]

    print(cost)


if __name__ == "__main__":
    solve()
