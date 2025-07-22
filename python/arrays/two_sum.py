# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  

input_str = input("Nhập dãy số: ")
nums = list(map(int, input_str.split(' ')))

target = int(input("Nhập giá trị target: "))

result = two_sum(nums, target)
print("Chỉ số của 2 số có tổng =", target, "là:", result)
