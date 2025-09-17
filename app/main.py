from flask import Flask

from app.determiners.result_determiner import ResultDeterminer
from app.models.configuration.comparison_configuration import *
from app.models.configuration.result_configuration import *

app = Flask(__name__)

@app.route('/')
def run_determiner():
    #result_1 = example_1()
    result_2 = example_2()

    return str(result_2)

def example_1():
    and_comparisons = [Comparison("insurance_payer", "==", "Medicaid")]
    or_comparisons_limited = [
        Comparison("provider_type", "==", "MSW"),
        Comparison("provider_type", "==", "MHC")
    ]

    or_comparisons = [
        Comparison("provider_type", "==", "LCSW")
    ]
    grouped_comparisons = [GroupedComparison(and_comparisons,
                                             or_comparisons_limited,
                                             ClaimProviderConfiguration(False, True)
                                             ),
                           GroupedComparison(and_comparisons,
                                             or_comparisons,
                                             ClaimProviderConfiguration(True, False)
                                             )]

    result_determiner = ResultDeterminer(grouped_comparisons)
    determined_result = result_determiner.get_result({"insurance_payer": "Medicaid", "provider_type": "LCSW"})
    return determined_result

def example_2():
    and_comparisons = [Comparison("insurance_payer", "==", "Medicaid")]
    or_comparisons_limited = [
        Comparison("provider_type", "==", "MSW"),
        Comparison("provider_type", "==", "MHC"),
        GroupedComparison([Comparison("insurance_payer", "==", "Medicare"), Comparison("provider_type", "==", "CASAC")])
    ]

    or_comparisons = [
        Comparison("provider_type", "==", "LCSW")
    ]
    grouped_comparisons = [GroupedComparison(and_comparisons,
                                             or_comparisons_limited,
                                             ClaimProviderConfiguration(False, True)
                                             ),
                           GroupedComparison(and_comparisons,
                                             or_comparisons,
                                             ClaimProviderConfiguration(True, False)
                                             )]

    result_determiner = ResultDeterminer(grouped_comparisons)
    determined_result = result_determiner.get_result({"insurance_payer": "Medicaid", "provider_type": "LCSW"})
    return determined_result

if __name__ == '__main__':
    app.run()


