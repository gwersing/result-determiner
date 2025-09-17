
class ComparisonTestModel:
    """Class to use for testing against an instance of an object"""
    def __init__(self, color, dob, age):
        """
        Args:
            color (str): color to test against to test str equality
            dob (datetime): datetime to test against to test datetime equality
            age (int): int to test against int equality
        """
        self.color = color
        self.dob = dob
        self.age = age

