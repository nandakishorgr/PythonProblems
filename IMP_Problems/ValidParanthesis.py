#Solution is built Using STACK Data structure

class Solution:
    def isValid(self, str):
        stack=[]
        paranth_map = { ")":"(", "]":"[", "}":"{" }

        for ch in str:
            if ch in paranth_map:
                if stack and stack[-1]==paranth_map[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        #return True if not stack else False
        return not stack



str="{[]}(){}"
#str="()[]{}"
#str=")"
obj=Solution()
res=obj.isValid(str)
print(res)
#result is : True


#Time Complexity : O(n)
#Space Complexity : O(n)