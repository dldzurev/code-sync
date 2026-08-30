class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(arr,target,left,right):
            if left > right:
                return -1
            mid  = left + (right-left)//2
            if(arr[mid] == target):
                return mid
            elif(arr[mid] > target):
                return binary_search(arr,target,left,mid-1)
            else:
                return binary_search(arr,target,mid+1,right)
        
        return binary_search(nums,target,0,len(nums)-1)