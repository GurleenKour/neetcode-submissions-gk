class Solution:
    def removeElement(self, nums: List[int], val: int) -> list[int]:
        l = len(nums)
        k = 0
        for i in range(l):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k

