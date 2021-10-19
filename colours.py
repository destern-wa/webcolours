from random import randrange
import colourise


class Colours:
    """A list of random web colours"""

    def __init__(self, size=20):
        """Initialises the colours list

        :param size: Number of colours to put in the list
        """
        # Size of the list
        self.size = size
        # Create the random list of colours
        self.list = [self.random() for _ in range(size)]
        # Non-public property for the current index point within the list
        self._index = 0
        self.is_paused = False

    def randomise(self):
        # Recreate the random list of colours
        self.list = [self.random() for _ in range(self.size)]
        # Reset the index
        self._index = 0


    def next(self):
        """Gets the next colour, and it's complement, from the list

        :return: Tuple (next colour, next colour's complement)
        """
        # Get the current index, then increment it (looping back to 0 after the last index of the list)
        i = self._index
        self._index = (self._index + 1) % self.size
        return self.list[i], Colours.complement(self.list[i])

    @staticmethod
    def complement(web_colour):
        """Gets the compliment of a web colour

        :param web_colour: Web colour - a '#' followed by 6 hex digits
        :return: Compliment of the web colour
        """
        # Get the rgb components
        red, green, blue = Colours.to_rgb(web_colour)
        # Get the complement's rgb components
        red_c, green_c, blue_c = colourise.complement_rgb(red, green, blue)
        # Convert back to a web colour
        return Colours.from_rgb(red_c, green_c, blue_c)

    @staticmethod
    def to_rgb(web_colour):
        """Converts a web colour into red, green, blue component values

        :param web_colour:
        :return: Tuple (red value, green value, blue value)
        """
        # Get the components as decimal digits
        components = list(map(Colours.from_hex_digit, web_colour[1:]))
        # Convert to decimals
        red = components[0]*16 + components[1]
        green = components[2]*16 + components[3]
        blue = components[4]*16 + components[5]
        return red, green, blue

    @staticmethod
    def from_rgb(red, green, blue):
        """Converts red, green, blue component values into a web colour"

        :param red: red component value, 0 to 255
        :param green: green component, 0 to 255
        :param blue: blue component, 0 to 255
        :return web colour
        """
        hex_digits = list(map(Colours.to_hex_digit, [
            int(red // 16),
            int(red % 16),
            int(green // 16),
            int(green % 16),
            int(blue // 16),
            int(blue % 16)
        ]))
        return '#' + ''.join(hex_digits)

    @staticmethod
    def from_hex_digit(hex_digit):
        """Converts a hex digit between '0' and 'F' into a number 0 to 15

        :param hex_digit: Hex digit as a string
        :return: Number
        """
        # For 0 to 9, just convert from string to int
        if ord('0') <= ord(hex_digit) <= ord('9'):
            return int(hex_digit)
        # For A to F, add 10 to the offset from A
        elif ord('A') <= ord(hex_digit) <= ord('F'):
            offset_from_a = ord(hex_digit) - ord('A')
            return 10 + offset_from_a
        else:
            raise RuntimeError("Only hex digits 0 to F can be converted")

    @staticmethod
    def to_hex_digit(num):
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
            return chr(int(ord('A') + offset_from_a))

    @staticmethod
    def random():
        """Generates a random web colour

        :return: Random web colour
        """
        return Colours.from_rgb(randrange(255), randrange(255), randrange(255))


if __name__ == "__main__":
    # Test by creating an instance and printing out the colours
    cols = Colours()
    for c in cols.list:
        print(c, end=' ')

    print('\nSome conversions:')
    for c in ["#FFFFFF", "#000000", "#FF0000", "#00FF00", "#0000FF", "#01AF7D", "#777777"] + cols.list:
        print(c)
        r, g, b = Colours.to_rgb(c)
        print(f" - rgb=({r}, {g}, {b})")
        print(f" - Converted back is {Colours.from_rgb(r, g, b)}")
        print(f" - Compliment is {Colours.complement(c)}")
