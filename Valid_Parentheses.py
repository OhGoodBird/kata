#!/usr/bin/env python3

#https://www.codewars.com/kata/52774a314c2333f0a7000688

def valid_parentheses(string):
    stack = []
    for c in string:
        if(c == '('):
            stack.append(c)
        elif(c == ')'):
            if(len(stack) == 0):
                return False
            stack.pop()
    if(len(stack) != 0):
        return False
    return True
    
    
def main():
    assert(valid_parentheses("  (") == False)
    assert(valid_parentheses(")test") == False)
    assert(valid_parentheses("") == True)
    assert(valid_parentheses("hi())(") == False)
    assert(valid_parentheses("hi(hi)()") == True)
    
if(__name__ == '__main__'):
    main()
    
    
