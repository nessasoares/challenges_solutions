import pytest 

def is_nested(S):
    stack = []

    result = 1
    open = ['(', '{', '[']
    close = [')', '}', ']']

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

class TestBrackets():
    def test_nested_examples(self):
        S = "{[()()]}"
        assert 1 == is_nested(S)

    def test_not_nested_examples(self):
        S = "([)()]"
        assert 0 == is_nested(S)

    def test_not_allowed_string(self):
        S = "([+h)()]"
        assert 0 == is_nested(S)

    