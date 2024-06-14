class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    """ 
    Manually defining what the string representation for this class would be, to
    return human readable output
    """

    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output

    # Less than operator for class Height
    def __lt__(self, other):
        height_inches_A = self.feet * 12 + self.inches

        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A < height_inches_B

    # Less than or equal to operator for class Height
    def __le__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A <= height_inches_B

    # Equal operator for class Height
    def __eq__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A == height_inches_B

    # Greater than operator for class Height
    def __gt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A > height_inches_B

    # Greater than or equal to operator for class height
    def __ge__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A >= height_inches_B

    # Not equal to operator for class Height
    def __ne__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A != height_inches_B


# Testing the methods against the test cases
print("Height(4, 5) < Height(4, 6): ", Height(4, 5) < Height(4, 6))
print("Height(4, 5) <= Height(4, 5): ", Height(4, 5) <= Height(4, 5))
print("Height(5, 10) == Height(5, 10): ", Height(5, 10) == Height(5, 10))
print("Height(4, 6) > Height(4, 5): ", Height(4, 6) > Height(4, 5))
print("Height(4, 5) >= Height(4, 5): ", Height(4, 5) >= Height(4, 5))
print("Height(4, 5) >= Height(4, 5): ", Height(4, 5) >= Height(4, 5))
print("Height(5, 9) != Height(5, 10): ", Height(5, 9) != Height(5, 10))

# Creating a list of Height objects
heights = [
    Height(5, 9),
    Height(4, 11),
    Height(5, 10),
    Height(4, 9),
]

# sorting the list of heights
heights = sorted(heights)

# printing the sorted heights
print("Sorted Heights: ")
for height in heights:
    print(height)
