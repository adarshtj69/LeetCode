class Solution:
    def romanToInt(self, s: str) -> int:
        romandict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,   'M':1000}
        prev=0
        total=0
        for ch in reversed(s):
            value=romandict[ch]
            if value<prev:
                total-=value
            else:
                total=total+value
                prev= value

        return total



