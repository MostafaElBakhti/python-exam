    # def twister(nums, n):
    #     if not nums:
    #         return []

    #     n = n % len(nums)
    #     return nums[-n:] + nums[:-n]

            

    # print(twister([1,2,3,4], 2))    


def twist_sequence(arr: list[int], k: int) -> list[int]:

    if not arr:
        return []

    k = k % len(arr)
    return arr[-k:] + arr[:-k]
# Basic cases
print(twist_sequence([1, 2, 3, 4, 5], 0))
# # [4, 5, 1, 2, 3]

print(twist_sequence([4, 2, 1, -1, 'a'], 4))
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