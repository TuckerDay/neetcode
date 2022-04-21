# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}

        for ch in s:
            dict_s[ch] = dict_s.get(ch, 0) + 1

        for ch in t:
            dict_t[ch] = dict_t.get(ch, 0) + 1

        for key in dict_s:
            if (not dict_t.has_key(key)) or (dict_s[key] != dict_t[key]):
                return False

        return True
