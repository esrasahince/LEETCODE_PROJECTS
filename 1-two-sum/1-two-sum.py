class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, val in enumerate(nums[:len(nums)-1]):
            a=target-val
            new=nums[idx+1:]
            if a in new:
                return[idx,new.index(a)+idx+1]
        