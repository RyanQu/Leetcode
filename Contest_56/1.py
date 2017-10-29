class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits)==0: return False
        if len(bits)==1:
            if bits[0]==0:
                return True
            else:
                return False
            
        result=[]  
        i=0
        while i<len(bits):
            if bits[i]==0:
                result.append([0])
                i=i+1
            else:
                result.append([1,bits[i+1]])
                i=i+2
            
        if result[-1]==[0]:
            return True
        else:
            return False