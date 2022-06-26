class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = set()
        
        n = len(nums)
        
        i = 0
        while i < n - 2:
            target = -nums[i]
            
            j, k = 0 + 1, n - 1
            
            while j < k:
                if nums[j] + nums[k] == target:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
                    
            i += 1
            
        return list(ans)
            
        