#!/usr/bin/env python3


def zeros_slow(n):
    sum = 1
    while(n > 0):
        sum *= n
        n -= 1
        
    num = 0
    sum = str(sum)
    for idx in range(len(sum)-1, -1, -1):
        if(sum[idx] == '0'):
            num += 1
        else:
            break
            
    return num
    
def zeros(n):
    cnt = 0
    t = 5
    while(n / t >= 1):
        cnt += n // t
        t *= 5
    return cnt
    
def main():
    assert(zeros(0) == 0)
    assert(zeros(6) == 1)
    assert(zeros(30) == 7)
    
if(__name__ == '__main__'):
    main()
    
    
