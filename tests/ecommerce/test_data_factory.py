import unittest
from karta_benchmarks.evaluation_datasets.ecommerce.data_factory.factory import factory

class TestEcommerceDataFactory(unittest.TestCase):

    def setUp(self):
        # Setup code to initialize objects or state before each test
        self.data_instance = factory()

    def test_correct_data_structure(self):
        # Make sure that the data structure is a dictionary
        self.assertIsInstance(self.data_instance, dict)

if __name__ == '__main__':
    unittest.main() 