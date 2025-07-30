class Solution:
    def isPalindrome(self, s: str) -> bool:
        k =''.join(i.lower() for i in s if i.isalnum())
        return k == k[::-1]
