def solution(nums):
    nums.sort() 
    unique = set(nums) 
    return min(len(set(nums)), len(nums) // 2)
