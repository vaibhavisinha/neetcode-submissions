class Solution:
    def isPalindrome(self, s: str) -> bool:
        split = "".join(s.split(" "))
        print(split)
        i,j=0,len(split)-1

        while i<j:
            if not self.isalnum(split[i]):
                i+=1
                continue
            if not self.isalnum(split[j]):
                j -=1
                continue
            if split[i].lower()!=split[j].lower(): return False
            i+=1
            j-=1 
        return True

    def isalnum(self,c):
        return( ord('A')<=ord(c)<=ord('Z') or
        ord('a')<=ord(c)<=ord('z') or 
        ord('0')<=ord(c)<=ord('9') )