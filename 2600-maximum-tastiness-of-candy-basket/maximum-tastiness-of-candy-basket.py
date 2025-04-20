class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        left,right, answer= 0,price[-1] - price[0],0
        """We have to maximize diff of consecutive candies.
        Can we pick k candies such that the minimum difference between any two of them is at least x?"""
        def check(mid):
            count=1
            prev=price[0]
            ind=1
            while (ind <len(price) and count <k):
                if price[ind] -prev>=mid:
                    prev=price[ind]
                    count +=1
                ind +=1
            return count==k

        while(left<=right):
            mid=(left+right)//2
            if check(mid):
                left=mid+1
                answer=mid
            else:
                right=mid-1
        return answer
        


    

    
        