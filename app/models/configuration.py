from enum import Enum
import operator


class Equality(Enum):
    EQUALS = operator.eq
    NOT_EQUALS = operator.ne
    LESS_THAN = operator.lt

class Comparison:
    operators = {
        "==": operator.eq,
        "!=": operator.ne,
        "<": operator.lt,
        "<=": operator.le,
        ">": operator.gt,
        ">=": operator.ge,
    }
    def __init__(self, property_name, comparison_type, comparison_value):
        self.property_name = property_name
        self.comparison_type = comparison_type
        self.comparison_value = comparison_value

    def __eq__(self, other):
        if (hasattr(other, self.property_name) and
                self.comparison_type in Comparison.operators
                and Comparison.operators[self.comparison_type](self.comparison_value, getattr(other, self.property_name))):
            return True
        else:
            return False

    def __hash__(self):
        return f'Comparison_{self.property_name}_{self.comparison_type}_{self.comparison_value}'

class GroupedComparison:
    def __init__(self, and_comparisons, or_comparisons, result):
        self.and_comparisons = and_comparisons
        self.or_comparisons = or_comparisons
        self.result = result

    def __eq__(self, other):
        and_comparisons_passed = True
        if self.and_comparisons is not None:
            for a in self.and_comparisons:
                if not a == other:
                    and_comparisons_passed = False  # TODO: Break out of upper loop and go to next grouped comparison
                    break

        or_comparison_passed = False
        # all and comparisons passed
        if and_comparisons_passed and self.or_comparisons is not None:
            for o in self.or_comparisons:
                if self == other:
                    or_comparison_passed = True
                    break

        comparison_passed = and_comparisons_passed and or_comparison_passed

        return comparison_passed

# class ComparisonStep(NextStep):
#     def __init__(self):
#         self.comparison = Comparison()
#         self.step_when_yes = NextStep()      #set to Comparison or result
#         self.step_when_no = NextStep()      #set to Comparison or result
#
# class Result(NextStep):
#     def __init__(self):
#         self.json_data = ""

class ClaimProviderConfiguration:
    def __init__(self, use_attending_provider_npi, use_supervising_provider_npi):
        self.use_attending_provider_npi = use_attending_provider_npi
        self.use_supervising_provider_npi = use_supervising_provider_npi

    def __str__(self):
        return f'ClaimProviderConfiguration:use_attending_provider_npi:{self.use_attending_provider_npi},use_supervising_provider_npi:{self.use_supervising_provider_npi}'


