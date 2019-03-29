#!/usr/bin/env python3


def duplicate_encode(word):
    dict = {}
    for c in word:
        c = c.lower()
        try: dict[c] += 1
        except KeyError: dict[c] = 1
    
    result = ''
    for c in word:
        c = c.lower()
        if(dict[c] == 1):
            result += '('
        else:
            result += ')'
            
    return result
    
def main():
    print(duplicate_encode("Success"))
    assert(duplicate_encode("din") == "(((")
    assert(duplicate_encode("recede") == "()()()")
    assert(duplicate_encode("Success") == ")())())")
    assert(duplicate_encode("(( @") == "))((")
    
if(__name__ == '__main__'):
    main()
    
    
