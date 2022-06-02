from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for t in nums:
            count[t] = 1+ count.get(t, 0)
        for key, val in count.items():
            freq[val].append(key)
        res = []
        print(freq, count)

        for i in range(len(freq)-1, 0, -1):
            if freq[i]!= []:
                res += freq[i]
                if len(res) == k:
                    return res

nums = [1,2]
k = 2
print(Solution().topKFrequent(nums, k))