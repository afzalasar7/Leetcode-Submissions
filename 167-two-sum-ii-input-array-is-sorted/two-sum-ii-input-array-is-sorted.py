class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(1,len(numbers)+1):
            x = target - numbers[i-1]
            l, r = i+1, len(numbers)
            while l<=r:
                mid = (l+r)//2
                if numbers[mid-1] == x:
                    return [i, mid]
                elif numbers[mid-1] < x:
                    l = mid+1
                else:
                    r=mid-1