class Solution:
    def reverseBits(self, n: int) -> int:
        bit_string = ""

        for i in range(32):
            bit_value = str((n >> i) & 1)
            bit_string += bit_value

        return int(bit_string, 2)