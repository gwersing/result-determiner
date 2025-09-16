# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask
from app.models.configuration.comparison_configuration import *
from app.models.configuration.result_configuration import *

app = Flask(__name__)

@app.route('/')
def run_determiner():

    and_comparisons = [Comparison("insurance_payer", "=", "Medicaid")]
    or_comparisons = [
        Comparison("provider_type", "=", "MSW"),
        Comparison("provider_type", "=", "MHC")
    ]
    result = ClaimProviderConfiguration(False, True)
    grouped_comparison = GroupedComparison(and_comparisons,
                                            or_comparisons,
                                            result
                                           )



    return f'Hi'  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
