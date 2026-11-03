# def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
#         if k==0:
#             return False
#         for i in range(0,len(nums)):
#             for j in range(i+1, i+k+1):
#                 if j<len(nums):
#                     if (nums[j] == nums[i]):
#                         return True
#                 elif (not (len(nums)-i<=1)):
#                     continue
#                 else:
#                     return False

# def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
#         t = []
        
#         for i in range(k, len(nums), 2*k+1):
#             for j in range(i-k,i+k+1):
#                 if j<len(nums):
#                     t.append(nums[j])
#                 else:
#                     return False

#                 t_set = set(t)
#                 if len(t_set) < len(t):
#                     return True
#                 else:
#                     t.clear()
#                     del t_set


# print(containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))

# def missingNumber(nums: list[int]) -> int:
#         test = [j for j in range(0,len(nums)+1)]
#         for i in nums:
#             if i not in test:
#                 return i

# print(missingNumber(nums = [9,6,4,2,3,5,7,0,1]))