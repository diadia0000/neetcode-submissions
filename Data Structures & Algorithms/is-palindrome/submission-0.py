class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for i in s.lower():
            if (ord("a")<=ord(i) and ord(i)<=ord("z")) or (ord("0")<=ord(i) and ord(i)<=ord("9")):
                word+=i
        l,r = 0,len(word)-1
        while l<=r:
            #print(word[l],word[r])
            if word[l] != word[r]:
                return False
            l+=1
            r-=1
        return True
        