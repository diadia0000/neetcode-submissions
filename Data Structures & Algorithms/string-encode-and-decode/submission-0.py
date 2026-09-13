class Solution:
    def __init__(self):
        self.space = []
    def encode(self, strs: List[str]) -> str:
        word = "".join(strs)
        for i in strs:
            self.space.append(len(i))
        return word
    def decode(self, s: str) -> List[str]:
        ans = []
        start = 0
        for i in self.space:
            end = start+i 
            ans.append(s[start:end])
            start+=i
        return ans
