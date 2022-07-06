#Using built in function and using extra memory so the solution is less efficient

class Solution:
    def isPalindrome(self,str):

        newStr=''

        for ch in str:
            if ch.isalnum():
                newStr += ch.lower()

        return newStr == newStr[::-1]

s = "A man, a plan, a canal: Panama"
res=Solution().isPalindrome(s)
print(res)