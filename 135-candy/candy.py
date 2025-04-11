class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        candies = [1] * n  # everyone gets at least 1 candy
        for i in range(1,n): 
            if ratings[i]> ratings[i-1]: #left to right pass to check if child needs to have more candies than left neighbour
                candies[i]=candies[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]> ratings[i+1]: #right to left pass to check if child needs to have more candies than right neighbour
                candies[i]=max(candies[i],candies[i+1]+1)
        return (sum(candies))