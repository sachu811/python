class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dict={
            ')':'(',
            '}':'{',
            ']':'['
        }
        for b in s:
            if b in dict:
                brack=stack.pop() if stack else '#'
                if(dict[b]!=brack):
                    return False
            else:
                stack.append(b)
        return not stack

sol=Solution()
b="[{(})]"
print(sol.isValid(b))