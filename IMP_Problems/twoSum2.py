#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number
#a one-based array indexed array has its first item indexed as 1
print("This solution works only if the array is sorted")

class Solution:
    def twoSum(self, numbers,target):
        l=0
        r=len(numbers) - 1

        while l<r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

s=Solution()
numbers = [2,4,7,9,12,15]
target = 13
#numbers=[5,9,3,7,2,8] ===> "For this array this solution doesnt give correct result as it is unsorted"
#target=16

res=s.twoSum(numbers,target)
print(res)