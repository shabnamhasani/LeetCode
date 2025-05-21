"""Start at index 0
For each digit, loop over its letters
Append one letter, move to the next digit (index + 1)
When the string is as long as digits, add it to the result"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_char = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result=[]
        def backtrack(index, current):
            if index == len(digits):
                result.append(current)
                return 
            for char in digit_to_char[digits[index]]:
                backtrack( index+1, current+char)


        backtrack(0, "")
        return result