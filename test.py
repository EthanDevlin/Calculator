#ACTS IN LIEU OF MAIN MAIN UNTIL MAIN BECOMES BACKEND

import main

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
        testSplit = test.strip().split(":")
        result = main.resolve(testSplit[0])
        if (float(result)) != float(testSplit[1]):
            failCount+=1
            print("Failure: " + testSplit[0])
            print("Expected: " + testSplit[1]) # USE % FOR CLARITY
            print("Returned: " + str(result) + "\n")
    
    # Configure outputs
    successPercentage = (1 - failCount/len(testArray)) * 100
    print(str(failCount) + " failures, success percentage: " +str(successPercentage)+ "%")

