class Solution(object):
    def mySqrt(self, x):

        prev = 0
        curr = 1
        product = 1
        while(product <= x):
            prev = curr
            curr += 1
            product = curr * curr
        return prev
        
        """
        :type x: int
        :rtype: int
        """