class Solution(object):
    def com(self, A,B):
        m=0
        for j in range(len(A)):
            i=0
            while i+j<len(A) and i<len(B):
                count=0
                while i+j<len(A) and i<len(B) and A[i+j]==B[i]:
                    count+=1
                    i=i+1   
                m=max(m,count)
                i=i+1
        return m
                
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A)>len(B):
            return self.com(B,A)
        elif len(A)==len(B):
            return max(self.com(A,B),self.com(B,A))
        else:
            return self.com(A,B)
        
        
        