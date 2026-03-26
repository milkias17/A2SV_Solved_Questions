import sys

input = sys.stdin.readline


def backtrack(s, i, curset, powerset):
    if i >= len(s):
        powerset.append(curset.copy())
        return

    if s[i] == "?":
        curset.append("+")
        backtrack(s, i + 1, curset, powerset)
        curset[-1] = "-"
        backtrack(s, i + 1, curset, powerset)
    else:
        curset.append(s[i])
        backtrack(s, i + 1, curset, powerset)

    curset.pop()


def solve():
    s1 = input().strip()
    s2 = input().strip()

    correct = 0
    for char in s1:
        if char == "+":
            correct += 1
        else:
            correct -= 1

    powerset = []
    backtrack(s2, 0, [], powerset)

    count = 0
    for ans in powerset:
        cur = 0
        for char in ans:
            if char == "+":
                cur += 1
            else:
                cur -= 1
        if cur == correct:
            count += 1

    print(count / len(powerset))


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()