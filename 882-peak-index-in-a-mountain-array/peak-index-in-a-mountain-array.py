class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #return arr.index(max(arr))
        m = -1
        for i in arr:
            m = max(i, m)
        return arr.index(m)
        