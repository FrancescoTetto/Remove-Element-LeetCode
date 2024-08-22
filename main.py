class Solution(object):
    def removeElement(self, nums, val):
        k = 0

        for i in range(len(nums)):
           if nums[i] != val:
               nums[k] = nums[i]
               k += 1

        
        for ind in range(k, len(nums)):
            nums[ind] = "_"
        
        return k

solution = Solution()
nums = [3,2,2,3]
val = 3

k = solution.removeElement(nums, val)

print(k)
print(nums)


      
