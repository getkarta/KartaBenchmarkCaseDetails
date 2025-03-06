import unittest
from karta_benchmarks.evaluation_datasets.ecommerce.function_factory.factory import (
    factory,
)


class TestSummarizeReturns(unittest.TestCase):
    def test_summarize_returns(self):
        tools = factory()
        callable = tools["tool_mapping"]["summarize_returns"]
        summary = callable(["RET20240513"])
        # Asset that the summary has the correct keys
        self.assertIn("RET20240513", [*summary.keys()])
        self.assertIn("order_id", [*summary["RET20240513"].keys()])
        self.assertIn("return_reason", [*summary["RET20240513"].keys()])
        print(summary)


if __name__ == "__main__":
    unittest.main()
