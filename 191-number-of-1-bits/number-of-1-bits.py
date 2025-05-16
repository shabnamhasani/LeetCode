class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n % 2  # add 1 if last bit is 1
            n = n // 2      # shift right
        return count
            