class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # assumption:
        #   - You may assume that each input would have exactly one solution, and you may not use the same element twice.
        #
        # If a list is traversed, then there is the opportunity to record the value and index of an observed element.
        # This information can be recorded in a map with key-value pairing of element=>index.
        # If a + b => target then target - b => a.
        # By traversing the input, the complement can be computed at each iteration.
        # If the complement has been observed, then function can return the correct value.
        # Otherwise, a new entry must be made to the map for potential future use.
        #
        # time complexity:
        #   O(n) where n is the number of elements in nums
        # space complexity:
        #   O(m)  where m is the number of entries in the map
        #
        obs_map = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in obs_map:
                return [obs_map[complement], i]
            else:
                obs_map.update({n: i})
