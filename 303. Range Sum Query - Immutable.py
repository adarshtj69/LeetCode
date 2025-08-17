class NumArray:

    def __init__(self, nums: List[int]):
        self.pre=[0]
        running=0
        for x in nums:
            running+=x
            self.pre.append(running)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right+1]-self.pre[left]
        
