class Solution:
    def mySqrt(self, x: int) -> int:
        #We are looking for the largest integer mid such that mid * mid <= x
        if x < 2:
            return x
        
        left, right = 1, x // 2
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right  # right is the largest integer such that right^2 <= x
        