# Using Two Pointer Approach without extra space

class Solution:
    def isPalindrome(self, str):
        l = 0
        r = len(str) - 1

        while l < r :
            while l < r and not self.alphanum(str[l]):
                l += 1
            while l < r and not self.alphanum(str[r]):
                r -= 1
            if str[l].lower() != str[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


s = "A man, a plan, a canal: Panama"
res=Solution().isPalindrome(s)
print(res)