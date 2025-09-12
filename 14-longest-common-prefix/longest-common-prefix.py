class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = strs[0]

        for word in strs[1:]:
            n = min(len(commonPrefix), len(word))
            if n == 0:
                return ""
            for i in range(n, 0, -1):
                if commonPrefix[0:i] == word[0:i]:
                    commonPrefix = commonPrefix[0:i]
                    break
                if i == 1:
                    return ""
        return commonPrefix 

                