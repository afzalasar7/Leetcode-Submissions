class Solution:
    def search(self, A: List[int], key: int) -> bool:
        l, r = 1, len(A) - 2
        if A[0] == key or A[-1]==key:
                return True
        while l <= r:
            mid = (l + r) // 2

            if A[mid] == key:
                return True

            if A[l] == A[mid] == A[r]:   
                    l+=1
                    r-=1
                    continue
            if A[l] == A[mid]:
                l+=1
                continue
            
            if A[mid]>= A[l]:
                if A[l] <= key and key <= A[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if A[mid] <= key and key <= A[r]:
                    l=mid+1
                else:
                    r=mid-1
        return False
