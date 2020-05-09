#{ 
#Driver Code Starts
#Initial Template for Python 3

import math


 # } Driver Code Ends

#User function Template for python3

import math
##Complete this function
def digitsInFactorial(N):
    #Your code here
    fact=1
    while(N>1):
        fact=fact*N
        N-=1
    count= int(math.log(fact,10))+1
        
    return count  


#{ 
#Driver Code Starts.

def main():
    
    T=int(input())
    
    while(T>0):
        N=int(input())
        
        print(digitsInFactorial(N))
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends