from base64 import encode
import enum
from tempfile import tempdir
from typing import List

class Solution:
    ord_a = ord("a")
    def encode_string(self, str: str) -> str:
        res = [0]*26
        for char in str:
            res[ord(char)-self.ord_a]+=1
        res_str = ""
        for i, t in enumerate(res):
            if t!= 0:
                res_str += f"{chr(i+self.ord_a)}{t}"
        return res_str

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        temp = {}
        for str in strs:
            code = self.encode_string(str=str)
            if code not in temp:
                temp[code] = [str]
            else:
                temp[code].append(str)
        
        for k in temp.keys():
            res.append(temp[k])
        return res

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))
