class Solution:
    def build_dict(self, s: str) -> dict:
        res = {}
        for char in s:
            if char not in res:
                res[char] = 0
            else:
                res[char] += 1
        return res

    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = self.build_dict(s)
        dic_t = self.build_dict(t)
        print(dic_s, dic_t)
        return dic_s == dic_t


s = "rat"
t = "car"
a = Solution()
print(f"Output = {a.isAnagram(s, t)}")