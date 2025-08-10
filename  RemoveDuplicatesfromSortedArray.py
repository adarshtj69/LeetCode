class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if i  not in l:
                l.append(i)
        for i in range(len(l)):
                nums[i]=l[i]
        return len(l)   
