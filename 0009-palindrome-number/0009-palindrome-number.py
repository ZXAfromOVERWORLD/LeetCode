class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        num=0
        while(temp>0):
            ad=temp%10
            num=num+ad
            num*=10
            temp=temp//10
        num=num//10
        if (num==x):
            return True
        else:
            return False
            