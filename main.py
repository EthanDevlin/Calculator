# Ethan Devlin 2022 - Calculator

import operands


def isFloat(value):
    try:
        float(value)
        return True
    except (ValueError):
        return False

# Handle calculation error


def error():
    print("error")
    exit()

# Calculate and return single operator values


def compute(operator, operand1, operand2):
    print("COMPUTE: " + str(operand1) + " " + str(operator) + " " + str(operand2))
    x = float(operand1)
    y = float(operand2)
    switch = {
        "+": operands.add(x, y),
        "-": operands.subtract(x, y),
        "*": operands.multiply(x, y),
        "/": operands.divide(x, y),
    }
    solution = switch.get((operator), "Invalid input")
    if solution != "Error":
        print("SOLUTION: " + str(solution))
        return solution
    else:
        error()


# Parse input calculation string and return calculated value


def solve(input):
    print("SOLVE: " + input)
    if isFloat(input):
        return input

    resolvedValue = 0
    for i in range(len(input)-1, -1, -1):
        if input[i] not in "1234567890.":
            resolvedValue = compute(input[i], solve(input[:i]), solve(input[i+1:]))
            break
    return(resolvedValue)

# Verify and format input


def parseInput(input):
    return(input)

# Solve equation


def resolve(input):
    parsedInput = parseInput(input)
    solution = solve(parsedInput)
    print("ANSWER: " + str(solution) + "\n")
    return(solution)

# Execute primary application process


if __name__ == "__main__":
    # Initialise variables
    testArray = []
    failCount = 0

    # Collect tests
    testFile = open("tests.txt", "r")
    tests = testFile.readlines()
    for test in tests:
        testArray.append(test)
    
    # Run tests
    for test in testArray:
        testSplit = test.strip().replace(" ", "").split(":")
        result = resolve(testSplit[0])
        if (float(result)) != float(testSplit[1]):
            failCount+=1
            print("Failure: " + testSplit[0])
            print("Expected: " + testSplit[1])
            print("Returned: " + str(result) + "\n")
    
    # Configure outputs
    successPercentage = (1 - failCount/len(testArray)) * 100
    print(str(failCount) + " failures, success percentage: " +str(successPercentage)+ "%")
