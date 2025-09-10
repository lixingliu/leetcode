class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        list1 = list(num1)
        list2 = list(num2)
        ans = ""
        zero = ord("0")
        n = len(list1)
        m = len(list2)
        big = max(n, m)
        extra = [0] * big
        if n > m:
            for _ in range(n-m):
                list2.insert(0, "0")
        if m > n:
            for _ in range(m-n):
                list1.insert(0, "0")
        for i in range(big - 1, -1, -1):
            sum = (ord(list1[i]) - zero) + (ord(list2[i]) - zero) + extra[i]
            if i == 0:
                ans = str(sum) + ans
                break
            if sum > 9:
                ans = str(sum - 10) + ans 
                extra[i-1] = 1
            else:
                ans = str(sum) + ans
        return ans  
