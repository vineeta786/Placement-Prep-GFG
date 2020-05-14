#{ 
#Driver Code Starts
#Initial Template for Python 3


import math



 # } Driver Code Ends

#User function Template for python3

##Complete this function
def modInverse(a,m):
    c=0
    for i in range(m):
        if((i*a)%m==1):
            c=i
            break
    if(c):
        return c
    else:
        return '-1'
    


#{ 
#Driver Code Starts.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        am=[int(x) for x in input().strip().split()]
        a=am[0]
        m=am[1]
        print(modInverse(a,m))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends