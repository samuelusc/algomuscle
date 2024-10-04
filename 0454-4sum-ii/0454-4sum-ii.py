class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict1 = {}
        count = 0
        for i in nums1:
            for j in nums2:
                dict1[i+j]= dict1.get(i+j, 0) + 1
        
        for x in nums3:
            for y in nums4:
                target = -(x+y)
                count += dict1.get(target, 0)
        
        return count