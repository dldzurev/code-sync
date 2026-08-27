class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,1,2,6]
        #[24,12,4,1]
        list_length = len(nums)
        left_list = [1] * list_length
        right_list = [1] * list_length
        for i in range (list_length):
            #populate left

            if(i>0):
                left_list[i] = left_list[i-1]*nums[i-1]
            
                right_list[list_length -1 -i] = right_list[list_length -i] * nums[list_length -i]

        for i in range(list_length):
            nums[i] = left_list[i]*right_list[i]
        return nums