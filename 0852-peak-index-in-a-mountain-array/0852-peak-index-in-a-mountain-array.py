class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left=0
        right=len(arr)-1
        while left<right:
            mid=(left+right)//2

            if arr[mid]>arr[left]:
                left+=1
            elif arr[mid]>arr[right]:
                right-=1
            
                
        return left
                
            