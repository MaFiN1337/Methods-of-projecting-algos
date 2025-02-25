import json

class MealyMachine:
    def __init__(self, mealy_schema_file, saved_state_file=None):
        with open(mealy_schema_file, "r") as f:
            mealy_schema = json.load(f)
        self.alphabet = mealy_schema["alphabet"]
        self.states = mealy_schema["states"]
        self.transitions = mealy_schema["transitions"]
        self.current_state = mealy_schema["init_state"]
        self.history = []
        if saved_state_file is not None:
            with open(saved_state_file, "r") as f:
                saved_state = json.load(f)
            self.current_state = saved_state["current_state"]
            self.history = saved_state["history"]

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
            self.history.append((self.current_state, symbol, output_symbol))
            print(f"input state: {self.current_state}", f"symbol: {symbol}",
                  f"new state: {new_state}", f"output: {output_symbol}" )
            self.current_state = new_state
        return output
    def save_state(self, file_name):
        state_data = {
            "current_state": self.current_state,
            "history": self.history,
        }
        with open(file_name, "w") as f:
            json.dump(state_data, f, indent=4)
        print(f"saved state to {file_name}")

if __name__ == "__main__":
    machine = MealyMachine("Mealy.json")
    input_str = "abba"
    machine.process_string(input_str)
    machine.save_state("Saved_state.json")