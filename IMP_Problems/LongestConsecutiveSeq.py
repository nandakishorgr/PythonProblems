class Solution:
    def longestConsecutive(self,nums):
        numSet=set(nums)
        longest_seq=0

        for n in nums:
            # check if its the start of a sequence
            if (n-1) not in numSet:
                length = 1
                while (n+length) in numSet:
                    length += 1
                longest_seq = max(length, longest_seq)
        return longest_seq



nums = [100,4,200,1,3,2]
res=Solution().longestConsecutive(nums)
print(res)
#result is : 4
