from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         solution = []
#         for i, _ in enumerate(nums):
#             for j, _ in enumerate(nums):
#                 print("i is %d, j is %d" , (i, j))
#                 if(nums[i] + nums[j] == target and i != j):
#                     solution.append(i)
#                     solution.append(j)
#                     return solution
#         return []    

# a = Solution();
# solution = a.twoSum([3,3], 6);
# print(solution)

#How do I do a for loop in python?
    # for i in nums
#I need to find two numbers in the list of nums that add up to the target
    # currently doing a double for loop
#The for loop returns the value, not the index for i, j. I need the index to print the indexes, not the actual values, how do I get the indexes?
    #use the enumerate function to get access to the index, and also the value is needed, for i, value in enumerate(nums):

#The solution above passes leet code, but it is O(n^2) and we can make this faster

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hash_map = {}
#         for i, value in enumerate(nums):
#             hash_map[value] = i
#         for i, value in enumerate(nums):
#             subtracted_value = target - value
#             if(subtracted_value in hash_map and i != hash_map[subtracted_value]):
#                 return [i, hash_map[subtracted_value]]
#         return []    

# a = Solution();
# solution = a.twoSum([3,3], 6);
# print(solution)

#We can use a hash map to track the values and indexes of the nums array, which in python is just using the {} notation
#This solution is faster but performs worse on memory, and we can improve by doing the hash mapping step inline

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, value in enumerate(nums):
            subtracted_value = target - value
            if(subtracted_value in hash_map):
                return [i, hash_map[subtracted_value]]
            hash_map[value] = i   

a = Solution();
solution = a.twoSum([3,3], 6);
print(solution)

#This solution adds after we tried to find a value that adds to the target. This inherently solves the issues where the same value has already been seen once but it exists twice in the list
#We dont need to check to make sure that the index isnt what was already there since we check before adding it to the list anyways, and break out if it was found twice and adds up to the target, ie 3,3 and 6