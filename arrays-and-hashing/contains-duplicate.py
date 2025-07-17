class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # A list composed entirely of unique elements has the same size as a set of those elements.
        # time complexity:
        #   O(n) where n is the number of elements in nums.
        #   time taken to construct a set from a list.
        # space complexity:
        #   O(n)
        #   space occupied by set.
        #
        return len(nums) != len(set(nums))
