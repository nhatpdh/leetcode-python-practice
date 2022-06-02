from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i, t in enumerate(nums):
            if target-t in temp:
                return [temp[target-t], i]
            else:
                temp[t] = i

a = Solution()
nums = [2,7,11,15]
target = 9
print(a.twoSum(nums, target))