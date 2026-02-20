from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        left = 0
        for right in range(len(nums)):
            if right - left + 1 == 3:
                if sorted_nums[left + 1] + sorted_nums[right] > sorted_nums[left]:
                    return (
                        sorted_nums[left] + sorted_nums[left + 1] + sorted_nums[right]
                    )

                left += 1

        return 0
