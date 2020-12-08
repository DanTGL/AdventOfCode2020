
inputs = [line.split() for line in open("day8/input").read().splitlines()]

def execute_code(code):
    accumulator = 0
    program_counter = 0
    executed_instructions = set()
    stack = list()
    corrupted = None

    while 0 <= program_counter < len(code):
        executed_instructions.add(program_counter)
        
        instr, arg = code[program_counter]
        count = 1
        if instr == "acc":
            accumulator += int(arg)

        else:
            count = int(arg) if instr == "jmp" else count
            
            if program_counter + count in executed_instructions:

                count = 1 if instr == "jmp" else int(arg)

                if corrupted == None:
                    corrupted = program_counter
                    stack.append((program_counter, accumulator, executed_instructions))

            elif corrupted == None:
                stack.append((program_counter, accumulator, executed_instructions))

                
        if program_counter + count in executed_instructions:
            if corrupted == program_counter:
                corrupted = None

            program_counter, accumulator, executed_instructions = stack.pop()

        program_counter += count
            
    return accumulator

print(execute_code(inputs))