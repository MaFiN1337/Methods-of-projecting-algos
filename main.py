import json

class MealyMachine:
    def __init__(self, mealy_schema_file):
        with open(mealy_schema_file, 'r') as f:
            mealy_schema = json.load(f)
        self.alphabet = mealy_schema['alphabet']
        self.states = mealy_schema['states']
        self.transitions = mealy_schema['transitions']
        self.current_state = mealy_schema['init_state']
    def process_string(self, input_string):
        output = ""
        for symbol in input_string:
            if symbol not in self.alphabet:
                raise ValueError(f"{symbol} not in alphabet")
            if self.current_state not in self.states:
                raise ValueError(f"{self.current_state} not in states")
            output_symbol = self.transitions[self.current_state][symbol][1]
            output += output_symbol
            new_state = self.transitions[self.current_state][symbol][0]
            print(f"input state: {self.current_state}", f"symbol: {symbol}", f"new state: {new_state}", f"output: {output_symbol}" )
            self.current_state = new_state
        return output

def main():
    machine = MealyMachine("Mealy.json")
    input_str = "abba"
    output_str = machine.process_string(input_str)
    print("Output string:", output_str)