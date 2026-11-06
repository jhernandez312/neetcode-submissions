class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dict: key = target - num, value = i

        store = {}
        for i, num in enumerate(nums):
            if num in store:
                return [store[num], i]
            store[target-num] = i
        return