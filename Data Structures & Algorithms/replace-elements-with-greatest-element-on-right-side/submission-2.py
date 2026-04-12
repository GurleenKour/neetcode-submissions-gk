class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxVal = -1

        for i in range(len(arr)-1,-1,-1):
            maxNum = max(arr[i],maxVal)
            arr[i] = maxVal
            maxVal = maxNum

        return arr