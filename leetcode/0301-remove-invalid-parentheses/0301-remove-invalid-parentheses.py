from typing import List


class Solution:
    def backtrack(self, s, i, stack, curset, powerset, visited):
        cur_str = "".join([s[idx] for idx in curset])
        state = (i, len(stack), cur_str)
        if state in visited:
            return
        visited.add(state)

        if i >= len(s) and not stack:
            if not powerset or len(cur_str) > len(powerset[-1]):
                powerset.clear()
                powerset.append(cur_str)
            elif len(curset) == len(powerset[-1]):
                powerset.append(cur_str)
            return
        elif i >= len(s):
            for y, o_idx in enumerate(stack):
                n_stack = stack.copy()
                n_stack.pop(y)
                for j, idx in enumerate(curset):
                    if idx < o_idx or s[idx] != "(":
                        continue
                    n_curset = curset.copy()
                    n_curset.pop(j)
                    self.backtrack(s, i, n_stack, n_curset, powerset, visited)

            return

        if s[i] != ")":
            if s[i] == "(":
                stack.append(i)
            curset.append(i)
            self.backtrack(s, i + 1, stack, curset, powerset, visited)
            curset.pop()
            if s[i] == "(":
                stack.pop()
            return

        curset.append(i)
        if not stack:
            for j, idx in enumerate(curset):
                char = s[idx]

                if char != ")":
                    continue

                n_curset = curset.copy()
                n_curset.pop(j)
                self.backtrack(s, i + 1, stack, n_curset, powerset, visited)
        else:
            cur_str = stack.pop()
            self.backtrack(s, i + 1, stack, curset, powerset, visited)
            stack.append(cur_str)

        curset.pop()

    def removeInvalidParentheses(self, s: str) -> List[str]:
        powerset = []
        self.backtrack(s, 0, [], [], powerset, set())
        return list(set(powerset))
