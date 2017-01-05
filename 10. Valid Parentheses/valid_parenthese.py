def valid_parentheses(string):
    # your code here

    if not string:
        return True
    else:
        stack = []
        for char in string:
            if char == '(':
                stack.append('(')
            elif char == ')':
                if not stack:
                    return False
                else:
                    stack.pop()
            else:
                continue
        if not stack:
            return True
        else:
            return False


print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses(""))
print(valid_parentheses("hi())("))
print(valid_parentheses("hi(hi)()"))


# Write a function called validParentheses that takes a string of
# parentheses, and determines if the order of the parentheses is valid.
# validParentheses should return true if the string is valid, and false if
# it's invalid.

# Examples:
# validParentheses( "()" ) => returns true
# validParentheses( ")(()))" ) => returns false
# validParentheses( "(" ) => returns false
# validParentheses( "(())((()())())" ) => returns true

# All input strings will be nonempty, and will only consist of open
# parentheses '(' and/or closed parentheses ')'
