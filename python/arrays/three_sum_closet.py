def threeSumCloset(nums, target):
    nums.sort()

    closet = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)-2):
        left = i + 1
        right = len(nums) - 1

        while(left < right):
            sum = nums[i] + nums[left] + nums[right]

            if(abs(target - closet)) >= (abs(target - sum)):
                closet = sum
            if(sum < target):
                left += 1
            else: right -= 1
    return closet


nums = list(map(int, input().split()))
target = int(input())
print(threeSumCloset(nums, target)) 