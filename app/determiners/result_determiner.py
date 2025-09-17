class ResultDeterminer:
    def __init__(self, grouped_comparison_config):
        """Will loop through the configured comparisons until it finds the first value result"""
        self.grouped_comparison_config = grouped_comparison_config

    def get_result(self, comparison_data):
        """
        Args:
            comparison_data (list[obj]): list of all comparisons to run sequentially
        Returns:
            result object in first GroupedComparison of configs that passes
        """
        result = None
        for i in self.grouped_comparison_config:
            if i == comparison_data:
                result = i.result
                break
        return result