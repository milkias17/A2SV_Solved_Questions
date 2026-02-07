from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for k, v in counter.items():
            if v != 2:
                return k
