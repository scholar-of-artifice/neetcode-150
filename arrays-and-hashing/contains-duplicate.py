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

#
# #
# # # ALTERNATIVE SOLUTION
# #
#
#
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         # Observe each value and add to a set to record observations.
#         # If a value is in the set, then it is a duplicate.
#         # time complexity:
#         #   O(n) where n is the number of elements in nums.
#         #   time taken to construct a set from a list.
#         # space complexity:
#         #   O(n)
#         #   space occupied by set.
#         #
#         obs_set = set()
#         for n in nums:
#             if n in obs_set:
#                 return True
#             else:
#                 obs_set.add(n)
#         return False
