class Solution:
    def create_id(self, s: str) -> tuple:
        # this particular id function returns a tuple where...
        # each index of the tuple represents a character in the...
        # range of characters for the input.
        #   this carries implicit assumptions about the input.
        # the value at a given index is the frequency count for that...
        # character.
        #
        # time complexity:
        #   O(n) where n is the length of the input string
        # space complexity:
        #   O(1)  the id is of constant size
        #
        id_list = [0] * (128)
        for c in s:
            idx = ord(c) - ord('a')
            id_list[idx] += 1
        return tuple(id_list)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # assumption:
        # the input can contain duplicate strings and the function will...
        # return each instance of that string in the output.
        #   example:
        #       ['abc', 'abc'] => [['abc', 'abc']]
        #
        # strings that are anagrams can be grouped as anagrams using a map.
        # the key-value pairing will be group_identifier => group_list.
        # the identifier can be a number of options.
        #   example:
        #        IF two strings are anagrams THEN they will be the same...
        # string when sorted.
        #        this string can be an identifier.
        #
        # IF strings are grouped together using a map THEN the output will...
        # be a list of the values for each keys.
        #
        # time complexity:
        #   O(n*k) where n is the number of strings in the input.
        #          where k is create_id
        # space complexity:
        #   O(m)  where m is the number of entries in the map
        #
        group_map = {}
        for s in strs:
            identifier = self.create_id(s)
            if identifier in group_map:
                group_map[identifier].append(s)
            else:
                group_map.update({identifier: [s]})
        return list(group_map.values())
