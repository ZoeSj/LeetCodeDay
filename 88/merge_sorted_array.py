def merge_sorted_array(nums_m, m, nums_n, n):
    num_m = nums_m[:m]
    num_n = nums_n[:n]
    test = sorted(num_m + num_n)
    print(test)


def merge(nums1, m, nums2, n):
    nums1[:] = nums1[:m]
    nums2[:] = nums2[:n]
    nums1.extend(nums2)
    nums1.sort()


# merge_sorted_array([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
merge_sorted_array([1], 1, [0], 0)
