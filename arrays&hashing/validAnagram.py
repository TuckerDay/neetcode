# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # If the strings are different lengths they cannot be annagrams
        if len(s) != len(t):
            return False

        # Create dictionaries for each word with the key as a letter and the
        # value as the number of times the letter occurs
        dict_s = {}
        dict_t = {}

        for ch in s:
            dict_s[ch] = dict_s.get(ch, 0) + 1

        for ch in t:
            dict_t[ch] = dict_t.get(ch, 0) + 1

        # Go through the keys in dict_s and see if dict_t has the same value for each key
        for key in dict_s:
            if (not dict_t.has_key(key)) or (dict_s[key] != dict_t[key]):
                return False

        return True
