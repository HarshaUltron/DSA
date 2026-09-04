class Solution:
    
    def infixToPostfix(self, s):
        
        # Define precedence of operators
        precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }
        
        stack = []      # Stores operators and parentheses
        result = []     # Stores the postfix expression
        
        # Process each character in the infix expression
        for char in s:
            
            # 1. If it is an operand, directly add it to the result
            if char.isalnum():
                result.append(char)
            
            # 2. If it is an opening parenthesis, push it onto the stack
            elif char == '(':
                stack.append(char)
            
            # 3. If it is a closing parenthesis,
            #    pop operators until '(' is found
            elif char == ')':
                
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                
                # Remove the '(' from the stack
                stack.pop()
            
            # 4. If it is an operator
            else:
                
                # Pop operators from the stack while:
                #
                # - Stack top is not '('
                # - Stack top has higher precedence
                # - OR same precedence and current operator is left-associative
                #
                # '^' is right-associative, so we do NOT pop
                # when both operators are '^'
                
                while (
                    stack
                    and stack[-1] != '('
                    and (
                        precedence[stack[-1]] > precedence[char]
                        or (
                            precedence[stack[-1]] == precedence[char]
                            and char != '^'
                        )
                    )
                ):
                    result.append(stack.pop())
                
                # Push current operator
                stack.append(char)
        
        # Pop all remaining operators from the stack
        while stack:
            result.append(stack.pop())
        
        # Convert result list into a string
        return ''.join(result)


df=Solution()
s="a+(b*c)"
print(df.infixToPostfix(s))    