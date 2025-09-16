class ResultDeterminer:
    def __init__(self, grouped_comparison_config):
        """Will loop through the configured comparisons until it finds the first value result"""
        self.grouped_comparison_config = grouped_comparison_config

    def get_result(self, comparison_data):
        result = None
        for i in self.grouped_comparison_config:
            if self.comparison_passes(i, comparison_data):
                result = i.result
                break
        return result


    #TODO: Move to __eq__ functionality
    def comparison_passes(self, comparison_config, comparison_data):
        return comparison_config == comparison_data
        # comparison_passed = False
        # if isinstance(comparison_config, Comparison):
        #     pass
        # elif isinstance(comparison_config, GroupedComparison):
        #     and_comparisons_passed = True
        #     if comparison_config.and_comparisons is not None:
        #         for a in comparison_config.and_comparisons:
        #             if not self.comparison_passes(a, comparison_data):
        #                 and_comparisons_passed = False  # TODO: Break out of upper loop and go to next grouped comparison
        #                 break
        #
        #     or_comparison_passed = False
        #     # all and comparisons passed
        #     if and_comparisons_passed and comparison_config.or_comparisons is not None:
        #         for o in comparison_config.or_comparisons:
        #             if self.comparison_passes(o, comparison_data):
        #                 or_comparison_passed = True
        #                 break
        #
        #     comparison_passed = and_comparisons_passed and or_comparison_passed
        # return comparison_passed