from karta_benchmarks.evaluation_datasets.ecommerce.task_factory.factory import factory

import unittest

class TestTaskLoader(unittest.TestCase):

    def setUp(self):
        self.tasks = factory()

    def test_tasks_not_empty(self):
        self.assertTrue(len(self.tasks) > 0, "The tasks list should not be empty.")

    def test_tasks_are_dicts(self):
        for task in self.tasks:
            self.assertIsInstance(task, dict, "Each task should be a dictionary.")

if __name__ == '__main__':
    unittest.main()
