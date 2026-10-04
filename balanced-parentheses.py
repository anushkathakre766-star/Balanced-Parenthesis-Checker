def is_balanced(expression: str) -> bool:
    stack = []
    # Map closing symbols to their corresponding opening symbols
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in matching_bracket.values():
            # If it's an opening symbol, push to the stack
            stack.append(char)
        elif char in matching_bracket.keys():
            # If it's a closing symbol, check against the stack
            if not stack or stack[-1] != matching_bracket[char]:
                return False
            stack.pop()
            
    # If stack is empty, all symbols matched properly
    return len(stack) == 0

# Test cases
print(is_balanced("(3 + 5) * [a + {b}]"))  # True
print(is_balanced("([{]})"))              # False