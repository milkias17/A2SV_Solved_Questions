class Solution:
    def is_good(self, position, m, distance):
        last_placed = position[0]
        count = 1

        for pos in position:
            if pos < last_placed + distance:
                continue
            count += 1
            last_placed = pos
        
        return count >= m

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 0
        right = position[-1]

        while left + 1 < right:
            mid = left + (right - left) // 2

            if self.is_good(position, m, mid):
                left = mid
            else:
                right = mid
        
        return left

        