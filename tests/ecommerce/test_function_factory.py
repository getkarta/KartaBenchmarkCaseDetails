import unittest
from karta_benchmarks.evaluation_datasets.ecommerce.function_factory.factory import factory

class TestEcommerceFunctionFactory(unittest.TestCase):

    def setUp(self):
        # Setup code to initialize objects or state before each test
        self.function_instance = factory()

    def test_get_date_difference(self):
        # Test a specific functionality
        callable = self.function_instance["tool_mapping"]["calculate_date_difference"]
        result = callable("2024-01-01", "2024-01-02")
        self.assertEqual(result, 1)
    
    def test_call_history(self):
        self.function_instance= factory()
        callable = self.function_instance["tool_mapping"]["calculate_date_difference"]
        result = callable("2024-01-01", "2024-01-02")
        # Get the call history and check that it has one entry
        call_history = self.function_instance["tool_mapping"]["get_call_history"]()
        self.assertEqual(len(call_history), 1)

if __name__ == '__main__':
    unittest.main() 