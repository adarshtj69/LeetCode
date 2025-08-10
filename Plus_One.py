class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
       n=0
       for i in digits:
         n=n*10+i
       n=n+1
       l=[]
       s=str(n)
       for i in s:
         l.append(int(i))
       return l
