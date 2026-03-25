from collections import defaultdict
import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    non_leafs = set()
    graph = defaultdict(list)

    for i in range(1, n):
        p = int(input())
        non_leafs.add(p)
        graph[p].append(i + 1)
        if i + 1 not in graph:
            graph[i + 1] = []

    for k, v in graph.items():
        if len(v) > 0:
            non_leafs.add(k)

    # print(f"Non_leaf: {non_leafs}")
    # print(f"Graph: {graph}")
    for non_leaf in non_leafs:
        # print(f"Checking {non_leaf}, {len(graph[non_leaf])}")
        count = 0
        for child in graph[non_leaf]:
            if len(graph[child]) == 0:
                count += 1
            if count >= 3:
                break
        if count < 3:
            print("No")
            return

    print("Yes")



def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()