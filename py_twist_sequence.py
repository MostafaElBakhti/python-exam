# def twister(nums, n):
#     if not nums:
#         return []
    
#     tool = len(nums)
#     n = n % tool

#     return nums[-n:] + nums[:-n]



def twister(nums , rot):
    if rot == 0:
        return nums
    result = []
    if rot > 0:
        print(nums)
        result = nums[-rot:]
        nums = [nums.pop() for _ in range(rot)]
        print(nums)
    return result + nums
        

print(twister([1,2,3,4], 2))

# Basic cases
# print(twister([1, 2, 3, 4, 5], 2))
# # [4, 5, 1, 2, 3]

# print(twister([4, 2, 1, -1, 'a'], 4))
# # [2, 1, -1, 'a', 4]

# # Rotation equal to length
# print(twister([1, 2, 3], 3))
# # [1, 2, 3]

# # Rotation greater than length
# print(twister([1, 2, 3], 5))
# # [2, 3, 1]

# # 3 1 2
# # 2 3 1 
# # 1 2 3 
# # 3 1 2 
# # 2 3 1 


# # Negative rotation (left rotation)
# print(twister([1, 2, 3, 4], -1))
# # [2, 3, 4, 1]

# # Edge cases
# print(twister([] , 3))
# # []

# print(twister([1], 10))
# # [1]