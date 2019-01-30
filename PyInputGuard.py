# TODO: add checking data directly(not using a prompt, example: x = enforceInt(someData))
# TODO: add length/size checking to enforceInt, enforceFloat, enforceString, ...?
# TODO: add precision checking to enforceFloat
# TODO: add enforceByte
# TODO: add enforceList
# TODO: add enforceTuple
# TODO: add enforceSet
# TODO: add enforceDictionary
# TODO: add documentation for methods
# TODO: add documentation in README
# TODO: add hardcore enforcement functions (loops until user gives valid input)
# TODO: add check for negative or positive numbers


import re

def enforceInt(prompt):
    testInput = input(prompt)
    try:
        testInput = int(testInput)
        return testInput
    except:
        return f'Input "{testInput}" cannot be converted into an integer.'

def enforceFloat(prompt):
    testInput = input(prompt)
    try:
        testInput = float(testInput)
        return testInput
    except:
        return f'Input "{testInput}" cannot be converted into a float.'

def enforceStringFormat(prompt, regex = None):
    testInput = input(prompt)
    if regex != None:
        pattern = re.compile(regex)
        if bool(pattern.match(testInput)):
            return testInput
        else:
            return f'Input "{testInput}" does not fit the specified format.'
    else:
        return testInput

def enforceBool(prompt):
    testInput = input(prompt)
    if testInput == 'True' or testInput == 'true':
        return True
    elif testInput == 'False' or testInput == 'false':
        return False
    else:
        return f'Input "{testInput}" cannot be converted to a boolean.'

def enforceComplex(prompt):
    testInput = input(prompt)
    testInput = testInput.replace(" ", "")
    try:
        return complex(testInput)
    except:
        return f'Input "{testInput}" cannot be converted into a complex number.'
