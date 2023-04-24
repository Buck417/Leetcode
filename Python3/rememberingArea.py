# This file is for retrying the python questions that were already answered. Retrying helps instill what is trying to be learned by doing these problems.


from typing import List

class Solution:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, value in enumerate(nums):
            if(target-value in hashmap):
                return [hashmap.get(target-value), i]
            hashmap[value] = i
solution = Solution();
print(solution.twoSum([2,7,11,15], 22));