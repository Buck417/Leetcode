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
solution = Solution();
print(solution.isPalindrome(12321));