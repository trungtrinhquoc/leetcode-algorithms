def removeDuplicates(nums):
    n = len(nums)
    i = 0
    for j in range(i+1, n):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1

num = list(map(int, input("Nhập mảng nums (cách nhau dấu cách): ").split()))

num.sort()

length = removeDuplicates(num)

print(*num[:length])