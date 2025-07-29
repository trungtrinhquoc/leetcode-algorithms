def findMedianSortedArrays(nums1, nums2):
    merged = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if (nums1[i] < nums2[j]):
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])
    n = len(merged)
    if(n % 2 == 1):
        return merged[n//2]
    else:
        return (merged[n//2 - 1] + merged[n // 2]) / 2
    
    
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
print('Median: ', findMedianSortedArrays(num1, num2))
