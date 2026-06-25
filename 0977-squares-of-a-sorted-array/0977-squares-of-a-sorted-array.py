class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[]
        left=0
        right=len(nums)-1

        while left<=right:
            temp1=nums[left]*nums[left]
            temp2=nums[right]*nums[right]

            if temp1>temp2:
                l.append(temp1)
                left+=1
            else:
                l.append(temp2)
                right-=1
        l.reverse()
        return l