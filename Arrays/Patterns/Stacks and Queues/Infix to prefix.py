class Solution:
    def infixToPrefix(self, s):
        #code here
            precedence = {
                '^': 3,
                '*': 2,
                '/': 2,
                '+': 1,
                '-': 1
            }

            stack = []
            result = []

            # Step 1: Reverse the expression
            s = s[::-1]

            # Step 2: Swap brackets
            s = ''.join(
                ')' if char == '(' else
                '(' if char == ')' else
                char
                for char in s
            )

            # Step 3: Convert reversed expression to postfix
            for char in s:

                # Operand
                if char.isalnum():
                    result.append(char)

                # Opening bracket
                elif char == '(':
                    stack.append(char)

                # Closing bracket
                elif char == ')':
                    while stack and stack[-1] != '(':
                        result.append(stack.pop())

                    # Remove '('
                    stack.pop()

                # Operator
                else:
                    while (
                        stack
                        and stack[-1] != '('
                        and (
                            precedence[stack[-1]] > precedence[char]
                            or (
                                precedence[stack[-1]] == precedence[char]
                                and char == '^'
                            )
                        )
                    ):
                        result.append(stack.pop())

                    stack.append(char)

            # Pop remaining operators
            while stack:
                result.append(stack.pop())

            # Step 4: Reverse postfix to get prefix
            return ''.join(result[::-1])