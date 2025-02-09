class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000} 
        P=0
        C=0
        result=0
        for i in s[::-1]:
            C=d[i]
            if C<P:
                result-=C
            else:
                result+=C
            P=C
        return result



