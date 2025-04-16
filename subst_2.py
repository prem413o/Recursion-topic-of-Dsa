class Solution(object):
    def subsetsWithDup(self, nums):
        ans=[]
        nums.sort()

        self.subset(nums, [],ans,0)
        return ans

    def subset(self,nums,current,ans,i):
        if(i==len(nums)):
            ans.append(current[:])
            return 

        current.append(nums[i])
        self.subset(nums,current,ans,i+1)

        current.pop()

        idx=i+1
        while idx<len(nums) and nums[idx]==nums[i]:
            idx+=1

        self.subset(nums,current,ans,idx)


solution=Solution()

print(solution.subsetsWithDup([1, 2, 2]))
        