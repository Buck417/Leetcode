from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]+nums[j] == target: return [i,j]

    def bestTwoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            if remaining in seen:
                return [i, seen[remaining]]
            else:
                seen[value] = i

solution = Solution();
print(solution.twoSum([3,3], 6));