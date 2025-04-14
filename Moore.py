class Moore:
    def __init__(self, states, input_alphabet, output_alphabet, transitions, initial_state, output_table):
        self.states = states
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.output_table = output_table

    def get_output_from_string(self, string):
        output = self.output_table[self.initial_state]
        current_state = self.initial_state
        for symbol in string:
            if symbol not in self.input_alphabet:
                raise ValueError(f"Invalid input symbol: {symbol}")
            current_state = self.transitions[current_state][symbol]
            output += self.output_table[current_state]
        return output