class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        dict_s = dict()
        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 1
        for char in t:
            if char in dict_s:
                dict_s[char] -= 1
                if dict_s[char] == 0:
                    dict_s.pop(char)
            else:
                return False
        print(dict_s)
        return True if len(dict_s) == 0 else False

            