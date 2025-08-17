class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currsum=0
        l=float('inf')
        slow=0
        for fast in range(len(nums)):
            currsum+=nums[fast]
            while currsum>=target:
                l=min(l,fast-slow+1)
                currsum-=nums[slow]
                slow+=1
        if l==float('inf'):
            return 0
        else:
            return l            
  
                
           


        
        