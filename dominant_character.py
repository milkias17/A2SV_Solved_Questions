import sys

input = sys.stdin.readline
print = sys.stdout.write


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input().strip()

        min_length = -1
        found = False
        for length in [2, 3, 4, 7]:
            for i in range(n - length + 1):
                sub = s[i : i + length]
                count_a = sub.count("a")
                count_b = sub.count("b")
                count_c = sub.count("c")

                if count_a > count_b and count_a > count_c:
                    min_length = length
                    found = True
                    break

            if found:
                break

        print(str(min_length) + "\n")


if __name__ == "__main__":
    solve()

