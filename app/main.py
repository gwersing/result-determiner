from flask import Flask, render_template

from app.determiners.result_determiner import ResultDeterminer
from app.models.configuration.comparison_configuration import *
from app.models.configuration.result_configuration import *
from collections import namedtuple

app = Flask(__name__)

@app.route('/')
def run_determiner():
    comparison_config = load_comparison_config()
    tests_to_run = load_tests_to_run()

    tests_ran = []

    CompletedTest = namedtuple('CompletedTest', 'comparison_data result')
    if tests_to_run is not None:
        result_determiner = ResultDeterminer(comparison_config)
        for test in tests_to_run:
            result = result_determiner.get_result(test)
            tests_ran.append(CompletedTest(test, result))

    data = {
        'comparison_config' : comparison_config,
        'tests_ran' : tests_ran
    }
    return render_template('index.html', **data)

def load_comparison_config():
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

    return grouped_comparisons

def load_tests_to_run():
    return [
        {"insurance_payer": "Medicaid", "provider_type": "LCSW"},
        {"insurance_payer": "Medicare", "provider_type": "MSW"},
        {"insurance_payer": "Medicaid", "provider_type": "MSW"}
            ]

if __name__ == '__main__':
    app.run(debug=True)


