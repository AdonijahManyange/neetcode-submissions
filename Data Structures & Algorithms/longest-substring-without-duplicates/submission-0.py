class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0 #l is left
        r = 0 #r is right
        res = 0

        for r in range(len(s)):
            #if the next char is a duplicate of another char in the str, then remove the char from the left and increment
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add (s[r]) #evaluate 
            res = max(res, r - l + 1)

        return res