from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        digitList = list(str(x));
        startIndex = 0;
        endIndex = len(digitList)-1;
        isPalindrome = True;
        while(startIndex < endIndex):
            if(digitList[startIndex] == digitList[endIndex]):
                startIndex +=1;
                endIndex -=1;
            else:
                isPalindrome = False;
                break;
        return isPalindrome;

    def goodIsPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0):
            return False;
        result = 0
        while x > result:
            result = result * 10 + x%10
            x = x//10
        return x == result or x == result // 10
solution = Solution();
print(solution.isPalindrome(12321));