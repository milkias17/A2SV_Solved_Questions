class Solution:
    def findUnion(self, a, b):
        # code here
        added = set()
        union = []
        for el in a:
            if el not in added:
                added.add(el)
                union.append(el)

        for el in b:
            if el not in added:
                added.add(el)
                union.append(el)

        return union
