
inputs = [line.split() for line in open("day8/input").read().splitlines()]

class Emulator:

    def __init__(self):
        self.accumulator = 0
        self.program_counter = 0
        self.executed_instructions = set()

    def execute_code(self, code):
        result = self.accumulator
        while self.program_counter < len(code):
            if self.program_counter in self.executed_instructions:
                return self.accumulator
            else:
                self.executed_instructions.add(self.program_counter)
                self.execute_instruction(code[self.program_counter])

        return result

    def execute_instruction(self, instruction):
        instr, arg = instruction

        if instr == "acc":
            self.accumulator += int(arg)
        elif instr == "jmp":
            self.program_counter += int(arg)
            return

        self.program_counter += 1

emulator = Emulator()
print(emulator.execute_code(inputs))
