class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numeral_map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "A":4, "B":9,
        "E":40, "F":90, "G":400, "H":900}
        s1 = s.replace("IV","A").replace("IX","B").replace("XL","E").replace("XC","F").replace("CD","G").replace("CM","H")
        li = list(s1)
        value = 0
        for i in li :
            value += numeral_map[i]  
        return value
#拿空间换时间，增加了内存但是减少了时间