class Solution:
    def reorderSpaces(self, text: str) -> str:
        output=''
        count=text.count(' ')
        lst=text.split()
        space_between,space_after=0,0
        n=len(lst)

        # Handle special case: only one word
        if n == 1:
            return lst[0] + ' ' * count

        space_between=count//(n-1)
        space_after=count%(n-1)
        output = (' ' * space_between).join(lst)
        output += ' ' * space_after
        return output

