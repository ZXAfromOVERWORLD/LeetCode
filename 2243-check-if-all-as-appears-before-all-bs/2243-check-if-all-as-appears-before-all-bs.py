class Solution:
    def checkString(self, s: str) -> bool:
        flag=0
        for i in s:
            if flag==1 and i=="a":
                return False
            elif i=="b":
                flag=1
            continue
        return True
            
        