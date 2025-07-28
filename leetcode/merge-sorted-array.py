class Solution(object):
    def merge(self, nums1, m, nums2, n):
        max1 = m
        max2 = n
        index_list = m + n 
        for i in range(index_list-1,-1,-1):
            if((m > 0) and (n > 0)):
                if(nums1[m-1] < nums2[n-1]):
                    nums1[i] = nums2[n-1]
                    n -= 1
                elif(nums1[m-1] > nums2[n-1]):
                    nums1[i] = nums1[m-1]
                    m -= 1
                else:
                    nums1[i] = nums1[m-1]
                    m -= 1
            elif n > 0:
                nums1[i] = nums2[n-1]
                n -= 1