#{ 
#Driver Code Starts
#Initial Template for Python 3


import math



 # } Driver Code Ends

#User function Template for python3


##Complete this function
def isPrime(N):
    #Your code here
    
    for v in range(2,N):
        if N%v==0:
            return False
    return True

#{ 
#Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        
        if(isPrime(N)):
            print("Yes")
        else:
            print("No")
            
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends