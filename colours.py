from random import randrange


class Colours:
    """A list of random web colours"""

    def __init__(self, size=20):
        """Initialises the colours list

        :param size: Number of colours to put in the list
        """
        self.list = [self.random() for _ in range(size)]

    @staticmethod
    def _to_hex_digit(num):
        """Converts a number between 0 and 15 into a hex digit

        :param num: Number
        :return: Hex digit as a string
        """
        if not (0 <= num <= 15):
            raise RuntimeError("Only numbers 0 to 15 can be converted into a hex digit")

        if num < 10:
            return str(num)
        else:
            # Calculate the offset from letter A
            offset_from_a = num - 10
            # Get the character at that offset
            return chr(ord('A') + offset_from_a)

    def random(self):
        # Generate 6 random hex digits
        hex_digits = [self._to_hex_digit(randrange(0, 16)) for _ in range(6)]
        # Join into a string prefixed with a hash
        return '#' + ''.join(hex_digits)


if __name__ == "__main__":
    """Test by creating an instance and printing out the colours"""
    cols = Colours()
    for c in cols.list:
        print(c, end=' ')
