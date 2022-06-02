from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for t in nums:
            if t not in check:
                check.add(t)
            else:
                return True
        return False

a = Solution()
nums = [1,2,3,1]
print(f"Output = {a.containsDuplicate(nums=nums)}")