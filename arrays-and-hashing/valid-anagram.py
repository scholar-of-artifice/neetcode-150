class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 strings s and t are anagrams if the contents of s can be rearranged to obtain an identical structure to t.
        # 2 maps (with key-value pairs char->int) will be identical if:
        #   - they use the same hashing algorithm
        #   - the input data is identical
        # time complexity:
        #   O(n + m) where n is the number of characters in s and where m is the number of characters in t.
        #   time taken to construct each map.
        # space complexity:
        #   O(n + m)  where n is the number of characters in s and where m is the number of characters in t.
        #   space taken to construct each map.
        #
        # Counter is a built-in collection in Python.
        return Counter(s) == Counter(t)

#
# #
# # # EQUIVALENT CODE
# #
#
# def isAnagram(self, s: str, t: str) -> bool:
#     return self.freq_map(s) == self.freq_map(t)
#
# def freq_map(self, s: str) -> dict:
#     out_map = {}
#     for c in s:
#         if c in out_map:
#             out_map[c] += 1
#         else:
#             out_map.update({c: 1})
#     return out_map
#
