def shift(index, nums1, filled):

    for i in range(filled - 1, index - 1, -1):
        nums1[i + 1] = nums1[i]

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        index1 = 0
        index2 = 0
        filled = m

        while index2 < n:
            if index1 < filled and nums1[index1] < nums2[index2]:
                index1 += 1
            else:
                shift(index1, nums1, filled)
                nums1[index1] = nums2[index2]
                filled += 1
                index1 += 1
                index2 += 1