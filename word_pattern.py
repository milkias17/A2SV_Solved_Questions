class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        splitted_s = s.split(" ")
        if len(splitted_s) != len(pattern):
            return False

        mapper = {}
        i = 0
        words_used = set()

        for char in pattern:
            if char not in mapper:
                if splitted_s[i] in words_used:
                    return False
                mapper[char] = splitted_s[i]
                words_used.add(splitted_s[i])
                i += 1
                continue

            if mapper[char] != splitted_s[i]:
                return False

            i += 1

        return True
