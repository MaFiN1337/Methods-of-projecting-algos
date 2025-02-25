from Abstract_machines import MealyMachine

if __name__ == "__main__":
    machine = MealyMachine("Mealy.json")
    input_str = "abba"
    machine.process_string(input_str)
    machine.save_state("Saved_state.json")