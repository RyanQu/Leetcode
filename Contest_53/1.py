def hasAlternatingBits(n):
    """
    :type n: int
    :rtype: bool
    """
    if n==0 or n==1:
        return False
    bin_str = bin(n)[2:] 
    for i in range(1,len(bin_str)):
        if bin_str[i]==bin_str[i-1]:
            return False

    return True

for i in range(50):
    x= hasAlternatingBits(i)
    print bin(i)[2:], x