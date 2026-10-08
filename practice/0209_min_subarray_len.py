def min_subarray_len(target: int, nums: list[int]) -> int:
    res = 1
    l = 0
    r = 1
    a = float("inf")
    tmp = nums[l]
    while l < r:
        if tmp < target and r < len(nums):
            tmp += nums[r]
            r += 1
            res += 1
        elif tmp >= target:
            a = min(res, a)
            tmp -= nums[l]
            l += 1
            res -= 1
        else:
            break
    if a == float("inf"):
        a = 0
    return a
