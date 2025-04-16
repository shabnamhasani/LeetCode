class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        """For each element, calculate its complement (target - current_element). check if the complement is already in the hash map"""
        hash_map={}
        for indx, key in enumerate(nums):
            Complement=target-key
            if Complement in hash_map:
                return [indx, hash_map[Complement]]
            hash_map[key]=indx



    