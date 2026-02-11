class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_x = list(str(x))
        length = len(list_x)
        if length == 1:
            return True
        num = ''
        i = 0
        while length > 1:
            
            if list_x[i] == '-':
                num = str(list_x[i]) + str(list[i+1])
            else:
                num = list_x[i]
            if num != list_x[-1]:
                return False
            else:
                list_x.pop(i)
                list_x.pop()
                length = length - 2
        return True

        