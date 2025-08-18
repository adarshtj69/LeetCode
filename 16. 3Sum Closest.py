class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestsum=0
        closest=float('inf')
        for i in range (len(nums)-2):
            l,r=i+1,len(nums)-1
            while l<r:
                currentsum=nums[i]+nums[l]+nums[r]
                diff=abs(target-currentsum)
                if diff<closest:
                    closest=diff
                    closestsum=currentsum
                if currentsum>target:
                    r-=1
                elif currentsum<target:
                    l+=1
                else:
                    return currentsum
        return closestsum
                
               
                
        