class Solution:
    def sortColors(self, nums: List[int]) -> None:
        a=b=c=0
        for num in nums:
            if num == 0:
                a+=1
            elif num==1:
                b+=1
            else:
                c+=1
        index=0
        for i in range(a):
            nums[index] = 0
            index+=1
        for i in range(b):
            nums[index] = 1
            index+=1
        for i in range(c):
            nums[index] = 2
            index+=1