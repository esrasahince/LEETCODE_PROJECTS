def process(nums1,nums2):
    result=[]
    for i in nums1:
        if i in nums2:
            result.append(i)
            nums2.remove(i)
    return result
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if(len(nums1)>=len(nums2)):
            return process(nums2,nums1)
        else:
             return process(nums1,nums2)
            
          
        
     
        
        