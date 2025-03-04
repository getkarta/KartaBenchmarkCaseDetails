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

    def test_get_package_details_failure(self):
        callable = self.function_instance["tool_mapping"]["get_package_details"]
        result = callable("PACK007898121")
        self.assertEqual(result, f"<error> Package with ID PACK007898121 not found </error>")

    def test_get_package_details_success(self):
        callable = self.function_instance["tool_mapping"]["get_package_details"]
        result = callable("PACK00789812")
        self.assertEqual(result["estimated_delivery_date"], "2024-05-27 10:00:00")

    def test_issue_gift_card_success(self):
        callable = self.function_instance["tool_mapping"]["issue_gift_card"]
        result = callable("CUST001001", 100)
        # Get a copy of the data
        mutated_data = self.function_instance["tool_mapping"]["get_db_state"]()
        self.assertEqual(mutated_data["payment_methods"]["GFT000001"]["amount_remaining"], 100)
        self.assertEqual(mutated_data["payment_methods"]["GFT000001"]["customer_id"], "CUST001001")
        self.assertEqual(mutated_data["payment_methods"]["GFT000001"]["payment_method_type"], "GIFT_CARD")

    def test_issue_gift_card_failure(self):
        callable = self.function_instance["tool_mapping"]["issue_gift_card"]
        result = callable("CUST001001", -100)
        self.assertEqual(result, f"<error> Amount must be positive </error>")   

    def test_issue_gift_card_failure_customer_not_found(self):
        callable = self.function_instance["tool_mapping"]["issue_gift_card"]
        result = callable("CUST0010011", 100)
        self.assertEqual(result, f"<error> Customer with ID CUST0010011 not found </error>")    
        
if __name__ == '__main__':
    unittest.main() 