from collections import Counter
from typing import List

class stack:
    def __init__(self):
        self.stack=[]
    def push(self,ele):
        self.stack.append(ele)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        self.stack[-1]
    def sizee(self):
        return len(self.stack) == 0
    def all_peek(self):
        return self.stack[:]

df=stack()
df.push(2)  
df.push(21)   
df.push(1322)  
print(df.all_peek())         
