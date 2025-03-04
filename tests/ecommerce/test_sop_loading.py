from karta_benchmarks.evaluation_datasets.ecommerce.sop.get_sops import sops
import unittest

class TestSopLoading(unittest.TestCase):
    def test_sop_loading(self):
        # Test that the SOPs are loaded correctly
        # Check to see if the "delayed_packages" SOP is loaded correctly
        # The sops() call must return a dictionary with the key as the file name (minus the extension)
        # and the value as the SOP content
        sop_dict = sops()
        self.assertEqual(len(sop_dict), 2)
        self.assertIn("delayed_packages", [*sop_dict.keys()])

if __name__ == "__main__":
    unittest.main()