import sys

input = sys.stdin.readline


def solve():
    seq = input().strip()
    stack = [-1]
    max_len = 0
    count = 1

    for i, char in enumerate(seq):
        if char == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                current_len = i - stack[-1]
                if current_len > max_len:
                    max_len = current_len
                    count = 1
                elif current_len == max_len and max_len > 0:
                    count += 1

    if max_len == 0:
        print("0 1")
    else:
        print(f"{max_len} {count}")


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()