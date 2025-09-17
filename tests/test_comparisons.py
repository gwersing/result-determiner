from datetime import datetime
from logging import raiseExceptions

import pytest
from app.models.configuration.comparison_configuration import *
from tests.models.comparison_models import *

@pytest.fixture
def sample_values():
    return {
        "color":"red",
        "dob": datetime(1990, 1, 1),
        "age":25
    }


@pytest.fixture
def sample_object(sample_values):
    return ComparisonTestModel(**sample_values)

class TestComparisonValues:
    #TODO: write tests for GroupedComparison
    #TODO: add in comments
    def test_comparison_invalid_comparison_type(self, sample_values):
        comparison =Comparison("color", "=!", "green")
        with pytest.raises(ValueError):
            passed = comparison == sample_values

    def test_comparison_eq_dict_str(self, sample_values):
        comparison =Comparison("color", "==", "red")
        assert comparison ==sample_values

    def test_comparison_eq_class_str(self, sample_object):
        comparison =Comparison("color", "==", "red")
        assert comparison == sample_object

    def test_comparison_eq_dict_datetime(self, sample_values):
        comparison =Comparison("dob", "==", datetime(1990,1,1))
        assert comparison ==sample_values

    def test_comparison_eq_class_datetime(self, sample_object):
        comparison =Comparison("dob", "==", datetime(1990,1,1))
        assert comparison == sample_object

    def test_comparison_eq_dict_int(self, sample_values):
        comparison =Comparison("age", "==", 25)
        assert comparison ==sample_values

    def test_comparison_eq_class_int(self, sample_object):
        comparison =Comparison("age", "==", 25)
        assert comparison == sample_object


    def test_comparison_ne_dict_str(self, sample_values):
        comparison =Comparison("color", "!=", "green")
        assert comparison ==sample_values

    def test_comparison_ne_class_str(self, sample_object):
        comparison =Comparison("color", "!=", "green")
        assert comparison == sample_object

    def test_comparison_ne_dict_datetime(self, sample_values):
        comparison =Comparison("dob", "!=", datetime(1991,1,1))
        assert comparison ==sample_values

    def test_comparison_ne_class_datetime(self, sample_object):
        comparison =Comparison("dob", "!=", datetime(1991,1,1))
        assert comparison == sample_object

    def test_comparison_ne_dict_int(self, sample_values):
        comparison =Comparison("age", "!=", 24)
        assert comparison ==sample_values

    def test_comparison_ne_class_int(self, sample_object):
        comparison =Comparison("age", "!=", 24)
        assert comparison == sample_object

    def test_comparison_lt_dict_datetime(self, sample_values):
        comparison =Comparison("dob", "<", datetime(1989,1,1))
        assert comparison ==sample_values

    def test_comparison_lt_class_datetime(self, sample_object):
        comparison =Comparison("dob", "<", datetime(1989,1,1))
        assert comparison == sample_object

    def test_comparison_lt_dict_int(self, sample_values):
        comparison =Comparison("age", "<", 24)
        assert comparison ==sample_values

    def test_comparison_lt_class_int(self, sample_object):
        comparison =Comparison("age", "<", 24)
        assert comparison == sample_object

    def test_grouped_comparison_eq_dict(self, sample_values):
        and_comparisons = [
            Comparison("color", "==", "red"),
            Comparison("age", ">=", 26)
        ]
        or_comparisons = [
            Comparison("dob", "<=", datetime(1990,1,1)),
            Comparison("dob", "<=", datetime(1989,1,1)),
        ]
        comparison = GroupedComparison(and_comparisons, or_comparisons, {})
        assert comparison ==sample_values

    def test_grouped_comparison_ne_dict(self, sample_values):
        and_comparisons = [
            Comparison("color", "==", "green"),
            Comparison("age", ">=", 26)
        ]
        or_comparisons = [
            Comparison("dob", "<=", datetime(1990,1,1)),
            Comparison("dob", "<=", datetime(1989,1,1)),
        ]
        comparison = GroupedComparison(and_comparisons, or_comparisons, {})
        assert comparison != sample_values

    def test_grouped_comparison_eq_class(self, sample_object):
        and_comparisons = [
            Comparison("color", "==", "red"),
            Comparison("age", ">=", 26)
        ]
        or_comparisons = [
            Comparison("dob", "<=", datetime(1990,1,1)),
            Comparison("dob", "<=", datetime(1989,1,1)),
        ]
        comparison = GroupedComparison(and_comparisons, or_comparisons, {})
        assert comparison ==sample_object

    def test_grouped_comparison_ne_class(self, sample_object):
        and_comparisons = [
            Comparison("color", "==", "green"),
            Comparison("age", ">=", 26)
        ]
        or_comparisons = [
            Comparison("dob", "<=", datetime(1990,1,1)),
            Comparison("dob", "<=", datetime(1989,1,1)),
        ]
        comparison = GroupedComparison(and_comparisons, or_comparisons, {})
        assert comparison != sample_object