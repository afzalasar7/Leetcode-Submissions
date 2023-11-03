class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        targetIndex = 0
        
        for i in range(1, n+1):
            if targetIndex == len(target):
                break  # No more elements to match in the target array
            
            if target[targetIndex] == i:
                operations.append("Push")
                targetIndex += 1
            else:
                operations.append("Push")
                operations.append("Pop")
        
        return operations