class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        print(nums)
        result=[]
        for first in range(len(nums)-2):
            if first==0 or nums[first-1]!=nums[first]:
                start=first+1
                end=len(nums)-1
                target=-nums[first]
                while start<end:
                    if nums[start]+nums[end]>target:
                        end-=1
                    elif nums[start]+nums[end]<target:
                        start+=1
                    else:
                        result.append([nums[first],nums[start],nums[end]])
                        start+=1
                        while nums[start-1]==nums[start] and start<end:
                            start+=1

                
        return result
