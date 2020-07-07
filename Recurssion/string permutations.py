#User function Template for python3
from itertools import permutations
##Complete this function
def permutation(S):
    ##Your code here
    s=list(set(list(permutations(S))))
    n = len(s)
    st = ["".join(s[i]) for i in range(n)]
    st.sort()
    for p in st:
        print(p,end=" ")




#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        S=input()
        permutation(S)
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends