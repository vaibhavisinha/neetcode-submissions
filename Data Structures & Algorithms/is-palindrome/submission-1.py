class Solution:
    def isPalindrome(self, s: str) -> bool:
        split = "".join(s.split(" "))
        print(split)
        i,j=0,len(split)-1

        while i<j:
            if not split[i].isalnum():
                i+=1
                continue
            if not split[j].isalnum():
                j -=1
                continue
            if split[i].lower()!=split[j].lower(): return False
            i+=1
            j-=1 
        return True