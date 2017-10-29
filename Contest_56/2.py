class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i=0
        while i<len(chars):
            count=1
            i=i+1
            while i<len(chars) and chars[i-1]==chars[i]:
                del chars[i]
                count=count+1
            
            str_count=""
            if count>1: 
                str_count=str(count)
                for j in range(len(str_count)):
                    chars.insert(i+j,str_count[j])
            i=i+len(str_count)
                    
        return len(chars)
        
            
        