import unittest
from Abstract_machines import MealyMachine, moore_to_mealy_converter

class TestMealyMachine(unittest.TestCase):
    def setUp(self):
        self.machine = MealyMachine("Mealy.json")

    def test_1(self):
        self.assertEqual(self.machine.process_string("a"), "0")

    def test_2(self):
        self.assertEqual(self.machine.process_string("b"), "0")

    def test_3(self):
        self.assertEqual(self.machine.process_string("ab"), "01")

    def test_4(self):
        self.assertEqual(self.machine.process_string("ba"), "00")

    def test_5(self):
        self.assertEqual(self.machine.process_string("abba"), "0100")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.machine.process_string("c")

class TestMooreToMealyConverter(unittest.TestCase):
    def setUp(self):
        moore_to_mealy_converter("Moore_to_mealy_schema.json")

    def test_random_strings(self):
        moore_machine = MealyMachine("Moore_to_mealy_schema.json")
        mealy_machine = MealyMachine("Mealy.json")

        test_strings = ["a", "b", "aa", "bb", "abab", "baba", "abba"]

        for test_str in test_strings:
            moore_output = moore_machine.process_string(test_str)
            mealy_output = mealy_machine.process_string(test_str)
            self.assertEqual(moore_output, mealy_output, f"Problem on input {test_str}")


if __name__ == "__main__":
    unittest.main()
