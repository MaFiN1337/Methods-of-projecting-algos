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

    def process_string(self, input_string) -> str:
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
    def save_state(self, file_name) -> None:
        state_data = {
            "current_state": self.current_state,
            "history": self.history,
        }
        with open(file_name, "w") as f:
            json.dump(state_data, f, indent=4)
        print(f"saved state to {file_name}")

class MooreMachine:
    def __init__(self, moore_schema_file):
        with open(moore_schema_file, "r") as f:
            moore_schema = json.load(f)
        self.alphabet = moore_schema["alphabet"]
        self.states = moore_schema["states"]
        self.transitions = moore_schema["transitions"]
        self.current_state = moore_schema["init_state"]
        self.states_output = moore_schema["states_output"]

    def process_string(self, input_string) -> str:
        output = ""
        for symbol in input_string:
            if symbol not in self.alphabet:
                raise ValueError(f"{symbol} not in alphabet")
            if self.current_state not in self.states:
                raise ValueError(f"{self.current_state} not in states")
            new_state = self.transitions[self.current_state][symbol]
            output_symbol = self.states_output[new_state]
            output += output_symbol
            print(f"input state: {self.current_state}", f"symbol: {symbol}",
                  f"new state: {new_state}", f"output: {output_symbol}")
            self.current_state = new_state
        return output

def moore_to_mealy_converter(moore_schema_file: str) -> None:
    with open(moore_schema_file, "r") as f:
        moore_schema = json.load(f)
    mealy_schema = { "alphabet": moore_schema["alphabet"], "states": moore_schema["states"], "transitions": {}, "init_state": moore_schema["init_state"] }
    for state, transitions in moore_schema["transitions"].items():
        mealy_schema["transitions"][state] = {}
        for symbol, next_state in transitions.items():
            output = moore_schema["states_output"][next_state]
            mealy_schema["transitions"][state][symbol] = [next_state, output]
    with open(moore_schema_file, "w") as f:
        json.dump(mealy_schema, f, indent=4)

