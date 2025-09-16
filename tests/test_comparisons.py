from datetime import datetime

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

@pytest.fixture
def sample_class_values():
    return ComparisonTestModel('red', datetime(1990, 1, 1), 25)

class TestComparisonValues:
    #TODO: write tests for all types, with all equalities
    #TODO: write tests for GroupedComparison
    #TODO: add in comments
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
