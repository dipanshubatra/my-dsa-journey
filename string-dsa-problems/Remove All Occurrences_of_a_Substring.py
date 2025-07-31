class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        k = len(part)
        def recurssion(m):
            if part in m:
                j = m.find(part)
                word = [ch for ch in m ]
                del word[j:j+k]
                z= ''.join(word)
                return recurssion(z)
            else:
                return m    
        return recurssion(s)
