def palindrome(n, k):
    for i in range(1, k + 1):
        rev = int(str(n)[::-1])       
        s = n + rev                  
        if str(s) == str(s)[::-1]:    
            return [i, s]
        n=s
    return [-1, -1]
n = 89
k = 30 
print(palindrome(n, k))
