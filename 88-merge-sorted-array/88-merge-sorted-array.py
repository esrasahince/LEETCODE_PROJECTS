def sizecheck(nums,m):
    del nums[m:]
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sizecheck(nums1,m)
        sizecheck(nums2,n)
        nums1+=nums2
        nums1.sort()
  
        