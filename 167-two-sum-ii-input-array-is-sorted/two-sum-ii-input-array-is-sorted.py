class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        sum=0
        start=0
        end=len(numbers)-1
        while start<end:
            if numbers[start]+numbers[end]==target:
                return [start+1,end+1]
            elif numbers[start]+numbers[end]>target:
                end-=1
            else:
                start+=1
        