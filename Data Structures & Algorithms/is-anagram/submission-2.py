from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = defaultdict(int)
        if len(s) != len(t):
            return False
        for c in s:
            char_map[c] +=1
        for c in t:
            count = char_map[c]
            if count==0:
                return False
            char_map[c] = count-1
        return True