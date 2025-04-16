class Solution(object):
    def subsets(self, nums):
        ans=[]
        self.generator(nums,[],0,ans)
        return ans

    def generator(self,nums,current,i,ans):
        if(i==len(nums)):
            ans.append(current[:])
            return

        current.append(nums[i])
        self.generator(nums,current,i+1,ans)

        current.pop()
        self.generator(nums,current,i+1,ans)
        

solution=Solution()
print(solution.subsets([1,2,3]))