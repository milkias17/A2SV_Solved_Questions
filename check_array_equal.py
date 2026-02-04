class Solution:
    def checkEqual(self, a, b) -> bool:
        # code here
        counter_a = {}
        counter_b = {}

        for el in a:
            counter_a[el] = counter_a.get(el, 0) + 1

        for el in b:
            counter_b[el] = counter_b.get(el, 0) + 1

        for k, v in counter_a.items():
            if k not in counter_b:
                return False
            if counter_b[k] != v:
                return False

        return True
