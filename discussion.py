#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    s=list(s)
    if(s[len(s)-2]=='P'):
        s.remove(s[len(s)-2])
        s.remove(s[len(s)-1])
        s="".join(s)
        t=[s.split(':')]
        k=t[0]
        if(k[0]=='12'):
            return ":".join(k)
        k[0]=str((int(k[0])+12)%24)
        return ":".join(k)
    else:
        s.remove(s[len(s)-2])
        s.remove(s[len(s)-1])
        s="".join(s)
        t=[s.split(':')]
        k=t[0]
        if(k[0]=='12'):
            k[0]=str((int(k[0])+12)%24)
            if(k[0]=='0'):
               k[0]='00'
        return ":".join(k)
    
if __name__ == '__main__':
    f = sys.stdout

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
