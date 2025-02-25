import unittest
from main import MealyMachine
import json

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mealy_schema = {
            "alphabet": ["a", "b"],
            "states": ["S0", "S1"],
            "transitions": {
                "S0": {"a": ["S1", "0"], "b": ["S0", "0"]},
                "S1": {"a": ["S1", "0"], "b": ["S0", "1"]}
            },
            "init_state": "S0"
        }
        with open("test_mealy_config.json", "w") as f:
            json.dump(mealy_schema, f, indent=4)
        cls.machine = MealyMachine("test_mealy_config.json")

    def test_1(self):
        self.assertEqual(self.machine.process_string("a"), "0")

    def test_2(self):
        self.assertEqual(self.machine.process_string("b"), "1")

    def test_3(self):
        self.assertEqual(self.machine.process_string("ab"), "01")

    def test_4(self):
        self.assertEqual(self.machine.process_string("ba"), "00")

    def test_5(self):
        self.assertEqual(self.machine.process_string("abba"), "0100")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.machine.process_string("c")

    def test_mixed_invalid_input(self):
        with self.assertRaises(ValueError):
            self.machine.process_string("abc")

if __name__ == '__main__':
    unittest.main()
