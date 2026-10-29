class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        # nums = self.nums.copy()
        self.nums.append(val)
        nums = self.nums.copy()
        nums.sort(reverse=True)
        print(nums)
        return nums[self.k-1]
        
