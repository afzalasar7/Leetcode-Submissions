class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        i = 0
                
        index = 0
        i = 1
        while i < len(colors):
            
            if colors[i] == colors[index]:
                
                if neededTime[i] >= neededTime[index]:
                    
                    res += neededTime[index]
                    
                    index = i
                    
                else:
                    
                    res += neededTime[i]
                    
            else:
                
                index = i
                    
            i += 1
            
        return res
                
                
                
            
            
                