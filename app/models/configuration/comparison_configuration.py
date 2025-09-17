import operator

class Comparison:
    """Class to compare any value (either in a dictionary or an attribute in an instance of a class) to an expected value"""
    operators = {
        "==": operator.eq,
        "!=": operator.ne,
        "<": operator.lt,
        "<=": operator.le,
        ">": operator.gt,
        ">=": operator.ge,
    }
    def __init__(self, property_name, comparison_type, comparison_value):
        """
        Args:
            property_name (str): name of attribute to compare against
            comparison_type (str): operator type to compare values
            comparison_value (object): expected value to compare against
        """
        self.property_name = property_name
        self.comparison_type = comparison_type
        self.comparison_value = comparison_value

    def __eq__(self, other):
        if self.comparison_type in Comparison.operators:
            value_to_compare = None
            if isinstance(other, dict) and self.property_name in other:
                value_to_compare = other.get(self.property_name)
            elif hasattr(other, self.property_name):
                value_to_compare = getattr(other, self.property_name)

            if Comparison.operators[self.comparison_type](self.comparison_value, value_to_compare):
                return True
            else:
                return False
        else:
            raise ValueError(f'{self.comparison_type} is not a valid comparison type')

    def __hash__(self):
        return f'Comparison_{self.property_name}_{self.comparison_type}_{self.comparison_value}'

class GroupedComparison:
    def __init__(self, and_comparisons, or_comparisons, result):
        """
        Args:
            and_comparisons (list[Comparison]): list of comparisons that all must return true to pass
            or_comparisons (list[Comparison]): list of comparisons that must have at least one true to pass
            result (object): object to return if comparisons passed
        """
        self.and_comparisons = and_comparisons
        self.or_comparisons = or_comparisons
        self.result = result

    def __eq__(self, other):
        and_comparisons_passed = True
        if self.and_comparisons is not None:
            for a in self.and_comparisons:
                if not a == other:
                    and_comparisons_passed = False
                    break

        or_comparison_passed = False
        # all and comparisons passed
        if and_comparisons_passed and self.or_comparisons is not None:
            for o in self.or_comparisons:
                if o == other:
                    or_comparison_passed = True
                    break

        comparison_passed = and_comparisons_passed and or_comparison_passed

        return comparison_passed

