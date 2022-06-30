#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:

    def merge(self,intervals):
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        merged=[]

        for interval in intervals:
            if not merged or merged[-1][1]<interval[0]:
                merged.append(interval)
            else:
                merged[-1][1]=max(merged[-1][1], interval[1])
        return merged


s=Solution()
intrls = [[1,3],[2,6],[8,10],[15,18],[10,13],[16,17]]
res=s.merge(intrls)
print(res)



#Time complexity :O(n log n)
#Space Complex: O(log n) or O(n)
