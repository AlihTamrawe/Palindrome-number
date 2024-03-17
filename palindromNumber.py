class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        lengt = len(y)-1
        for i in range (0,(len(y)-1)/2+1):
            if y[i] != y[lengt-i]:
                return False
        return True
        # result = 0
        # deg = 1
        # temp = x
        # while temp>=10:
        #     deg *=10
        #     temp/=10
        # temp= x
        # pw =1
        # while deg>0:
        #    result += x/deg *pw
        #    x=x%deg
        #    pw*=10
        #    deg/=10
        
        # if temp <0:
        #     return False
        # if temp == result:
        #     return True
        
        # return False

            
            

        