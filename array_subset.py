# User function Template for python3


class Solution:
    # Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        counter_a = {}
        counter_b = {}

        for el in a:
            counter_a[el] = counter_a.get(el, 0) + 1

        for el in b:
            counter_b[el] = counter_b.get(el, 0) + 1

        for k, v in counter_b.items():
            if k not in counter_a:
                return False
            if counter_a[k] < v:
                return False

        return True
