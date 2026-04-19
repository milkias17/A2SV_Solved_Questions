class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue

            target = -1 * num

            left = i + 1
            right = len(nums) - 1
            while left < right:
                cur = nums[left] + nums[right]
                if cur == target:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif cur > target:
                    right -= 1
                else:
                    left += 1
        
        return res
