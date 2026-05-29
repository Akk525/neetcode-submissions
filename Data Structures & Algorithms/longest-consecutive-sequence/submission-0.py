class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashed = set(nums)
        max_seq = 0

        for num in hashed:
            if num - 1 not in hashed:
                seq = 1
                cur_num = num

                while cur_num + 1 in hashed:
                    seq += 1
                    cur_num += 1

                max_seq = max(max_seq, seq)

        return max_seq