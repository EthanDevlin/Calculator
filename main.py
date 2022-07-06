# Ethan Devlin 2022 - Calculator

import operands

# Handle calculation error


def error():
    print("error")
    exit()
    
# Calculate and return single operator values


def compute(operator, operand1, operand2):
    x = float(operand1)
    y = float(operand2)
    switch = {
        "+": operands.sum(x,y),
        "-": x - y,
        "*": x * y,
        "/": operands.divide(x,y),
    }
    solution = switch.get((operator), "Invalid input")
    if solution != "Error":
        return solution
    else:
        error()



# Parse input calculation string and return calculated value


def solve(input):
    inputArray = input.split(" ")
    resolvedValue = compute(inputArray[1], inputArray[0], inputArray[2])
    return(resolvedValue)

# Verify and format input


def parseInput(input):
    return(input)

# Solve equation


def resolve(input):
    parsedInput = parseInput(input)
    solution = solve(parsedInput)
    return(solution)

# Execute primary application process


if __name__ == "__main__":
    print("hello world")
    print(resolve("4 + 2"))
