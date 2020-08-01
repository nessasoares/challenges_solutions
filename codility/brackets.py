import pytest 

def old_is_nested(S):
    stack = []

    result = 1
    open = ['(', '{', '[']
    close = [')', '}', ']']

    if not S:
        return 1

    if len(S) < 200000:
        for character in S:
            if character in open:
                stack.append(character)

            elif character in close:
                if stack:
                    opening = stack.pop()
                    closing = character

                    are_parenthesis = opening == '(' and closing == ')' 
                    are_brackets = opening == '[' and closing == ']' 
                    are_curly_brackets = opening == '{' and closing == '}'

                    if are_parenthesis or are_brackets or are_curly_brackets:
                        result = 1 
                    else:
                        result = 0 
            else:
                return 0
    else:
        result = 0
    
    return result


def is_nested(S):

    stack = []
    result = 0
    # S is empty
    if not S:
        return 1
    if len(S) > 200000:
        return 0

    open_options = ['{', '(', '[']
    closed_options =  ['}', ')', ']']

    is_open = lambda e: e in open_options
    is_closed = lambda e: e in closed_options
    
    for element in S:
        if is_open(element):
            stack.append(element)
        elif is_closed(element) and stack:
            current = element 
            previous = stack.pop()
            
            if open_options.index(previous) == closed_options.index(current):
                result = 1
            else:
                result = 0
        else:
            result = 0
            break
    
    if len(stack) > 0:
        result = 0

    return result

    # S has the form (U)

    # S has the form VW

class TestBrackets():
    def test_nested_examples(self):
        S = "{[()()]}"
        assert 1 == is_nested(S)

    def test_not_nested_examples(self):
        S = "([)()]"
        assert 0 == is_nested(S)

        S ="()(()()(((()())(()()))"
        assert 0 == is_nested(S)

    def test_not_allowed_string(self):
        S = "([+h)()]"
        assert 0 == is_nested(S)

    def test_cases(self):
         assert 1 == is_nested("{[()()]}")
         assert 1 == is_nested("{[(){([])}()]}")
         assert 1 == is_nested("{}")
         assert 1 == is_nested("()")
         assert 1 == is_nested("[]")
         assert 1 == is_nested("[([][])()]")
         assert 0 == is_nested("([)()]")
         assert 0 == is_nested("(]")
         assert 0 == is_nested("{{{{")
         assert 0 == is_nested(")))")

    