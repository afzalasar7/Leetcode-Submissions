class Solution:
    def majorityElement(self, nums: List[int]) -> int:        
    #    tc = O(n), sc = O(n)
    #    from collections import Counter
    #     hash = {}
    #     for i in nums:
    #         #hash[i] = hash.get(i, 0) +1
    #         if i in hash:
    #             hash[i] +=1
    #         else:
    #             hash[i] =1    
    #     major = len(nums)//2
    #     for i, v in hash.items():
    #         if v>major:
    #             return i
        cnt = 0
        major_element=None
        for i in nums:
            if cnt == 0:
                major_element = i
                cnt+=1
            elif major_element == i:
                cnt+=1
            else:
                cnt-=1
        return major_element