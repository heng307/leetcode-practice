def sorted_squares(nums: list[int]) -> list[int]:
    result = [0] * len(nums)
    l, r, p = 0, len(nums) - 1, len(nums) - 1
    while l <= r:
        if nums[l] * nums[l] > nums[r] * nums[r]:
            result[p] = nums[l] * nums[l]
            l += 1
        else:
            result[p] = nums[r] * nums[r]
            r -= 1
        p -= 1
    return result
