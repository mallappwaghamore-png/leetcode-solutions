class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        
        for num in nums:
            count[num]=count.get(num,0)+1
        mejority=0
        max_count=0
        for key in count:
            if count[key]>max_count:
                max_count=count[key]
                mejority=key
        return mejority
        
