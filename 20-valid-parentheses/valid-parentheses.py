class Solution(object):
    def isValid(self, s):
        stack = [] 
        pair = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s:
            if bracket in pair:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pair[stack.pop()]:
                return False
        return len(stack) == 0
        