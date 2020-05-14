#User function Template for python3

'''complete function to search pattern in the given string
   p: pattern given in input
   s: string given in the input'''
def search(p,s):
    #code here
    
    if s.find(p) > -1 :
        return True
        
    return False



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        if(search(p,s)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends