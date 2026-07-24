import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        chars = list(string.ascii_letters)
        chars.extend(map(str, range(10)))

        while i < j:
            if s[i] not in chars and s[j] not in chars:
                i += 1
                j -= 1
                continue 
            elif s[j] not in chars:
                j -= 1
                continue
            elif s[i] not in chars:
                i += 1
                continue
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True


        