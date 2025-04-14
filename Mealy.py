class Mealy:
    def __init__(self, states, input_alphabet, output_alphabet, transitions, initial_state):
        self.states = states
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.transitions = transitions
        self.initial_state = initial_state

    def get_output_from_string(self, string):
        output = ''
        current_state = self.initial_state
        for symbol in string:
            if symbol not in self.input_alphabet:
                raise ValueError(f"Invalid input symbol: {symbol}")
            next_state, out = self.transitions[current_state][symbol]
            output += out
            current_state = next_state
        return output