class Solution:
    def isValid(self, s: str) -> bool:
        d=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                d.append(i)
            elif i==")":
                if d==[]:
                    return False
                last=d.pop()
                if last !="(":
                    return False
            elif i=="}":
                if d==[]:
                    return False
                last=d.pop()
                if last !="{":
                    return False
            elif i=="]":
                if d==[]:
                    return False
                last=d.pop()
                if last !="[":
                    return False
        if d==[]:
            return True
        else:
            return False