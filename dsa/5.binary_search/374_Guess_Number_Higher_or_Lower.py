# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left: int = 1
        right: int = n

        while left <= right:
            mid: int = int((right - left) / 2) + left
            guess_result: int = guess(mid)
            if guess_result == 0:
                return mid
            elif guess_result == 1:
                left = mid + 1
            else:
                right = mid - 1
        

        return -1 