

class Puzzle1Solver(object):
    """A program that prints all sequences of binary digits, such that each
       digit in the sequence is a 0 or 1, and no sequence has two 1's adjacent
       in the output.
    """
    @classmethod
    def main(cls):

        num_bits = 32
        max = (1 << num_bits) - 1
        val = 0
        
        while (val <= max):
            is_valid = True

            # Detect if we have any runs with two consecutive bits set
            for bit_offset in range(0, num_bits - 1):
                if 0x3 == (val >> bit_offset) & 0x3:
                    # two bits are set, skip the known intermediates
                    # - we know that the first clash will always occur when the 
                    #   least-significant bit (or bits) are zero, so we can skip
                    #   in powers-of-two
                    val += 1 << bit_offset
                    is_valid = False
                    break

            if is_valid:
                print('Valid sequence: {:0{width}b}'.format(val, width=num_bits))
                val += 1

if __name__ == "__main__":
    Puzzle1Solver.main()
