nums = [1, 5, 8, 12, 20]

left = 0
right = len(nums) - 1

while left < right:
    if nums[left] + nums[right] == 21:
        print(nums[left])
        break
    elif nums[left] + nums[right] < 21:
        left += 1
    else:
        right -= 1