#!/usr/bin/env python3

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
    
    
