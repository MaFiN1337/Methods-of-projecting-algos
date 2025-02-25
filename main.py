import json

class MealyMachine:
    def __init__(self, mealy_schema_file):
        with open(mealy_schema_file, 'r') as f:
            mealy_schema = json.load(f)
        self.alphabet = mealy_schema['alphabet']
        self.states = mealy_schema['states']
        self.transitions = mealy_schema['transitions']
        self.current_state = mealy_schema['init_state']
