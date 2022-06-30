#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.Merge nums1 and nums2 into a single array sorted in non-decreasing order.

class Solution:
    def MergeSortArrays(self,nums1,m,nums2,n):
        #last index of nums1 (as problem says nums1 has extra space(m+n) to merge nums2)
        last=m+n-1

        # merge in reverse order
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
        # Fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[last] = nums2[n-1]
            n = n-1
            last = last-1

        return nums1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
obj=Solution()
res=obj.MergeSortArrays(nums1,m,nums2,n)
print(res)

# Fill nums1 with leftover nums2 elements scenario below is the input
#nums1 = [2,2,3,0,0,0]
#nums2 = [1,5,6]

#Time Complexity: O(n)
#Space Complexity: O(1)