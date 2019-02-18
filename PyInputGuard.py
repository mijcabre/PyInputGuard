# TODO: add enforceYesNo
# TODO: DRY/refactor code (minMaxValue, Use arrays for enforceBool)
# TODO: add check to make sure maxValue > minValue && maxLength > minLength
# TODO: add documentation for methods
# TODO: add documentation in README

import re

def enforceInt(prompt, minValue = None, maxValue = None):
    testInput = input(prompt)
    try:
        testInput = int(testInput)
        if minValue and maxValue:
            if testInput >= minValue and testInput <= maxValue:
                return testInput
            else:
                return f'Input "{testInput}" must be between {minValue - 1} and {maxValue + 1}.'
        elif minValue:
            if testInput >= minValue:
                return testInput
            else:
                return f'Input "{testInput}" is too small. Input must be at least {minValue}.'
        elif maxValue:
            if testInput <= maxValue:
                return testInput
            else:
                return f'Input "{testInput}" is too large. Input must be less than {maxValue + 1}.'
        else:
            return testInput
    except:
        return f'Input "{testInput}" cannot be converted into an integer.'

def enforceFloat(prompt, minValue = None, maxValue = None, precision = None):
    testInput = input(prompt)
    try:
        testInput = float(testInput)
        if precision != None:
            testInput = round(testInput, precision)
        if minValue and maxValue:
            if testInput >= minValue and testInput <= maxValue:
                return testInput
            else:
                return f'Input "{testInput}" must be between {minValue - 1} and {maxValue + 1}.'
        elif minValue:
            if testInput >= minValue:
                return testInput
            else:
                return f'Input "{testInput}" is too small. Input must be at least {minValue}.'
        elif maxValue:
            if testInput <= maxValue:
                return testInput
            else:
                return f'Input "{testInput}" is too large. Input must be less than {maxValue + 1}.'
        else:
            return testInput
        return testInput
    except:
        return f'Input "{testInput}" cannot be converted into a float.'

def enforceStringFormat(prompt,  regex = None, minLength = None, maxLength = None):
    testInput = input(prompt)
    if regex != None:
        pattern = re.compile(regex)
        if bool(pattern.match(testInput)):
            return testInput
        else:
           return f'Input "{testInput}" does not fit the specified format.'
    else:
        testInputLength = len(testInput)
        if minLength and maxLength:
            if testInputLength >= minLength and testInputLength <= maxLength:
                return testInput
            else:
                return f'Input "{testInput}" must be between {minLength - 1} and {maxLength + 1} characters long.'
        elif minLength:
            if testInputLength >= minLength:
                return testInput
            else:
                return f'Input "{testInput}" is too small. Input must be at least {minLength} characters long.'
        elif maxLength:
            if testInputLength <= maxLength:
                return testInput
            else:
                return f'Input "{testInput}" is too large. Input must be less than {maxLength + 1} characters long.'
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

def strictEnforceInt(prompt, minValue=None, maxValue=None):
    while(True):
        possibleInt = enforceInt(prompt, minValue, maxValue)
        if isinstance(possibleInt, int):
            break
        else:
            print(possibleInt + ' Try again.')
    return possibleInt

def strictEnforceFloat(prompt, minValue=None, maxValue=None, precision = None):
    while(True):
        possibleFloat = enforceFloat(prompt, minValue, maxValue, precision)
        if isinstance(possibleFloat, float):
            break
        else:
            print(possibleFloat + ' Try again.')
    return possibleFloat

def strictEnforceStringFormat(prompt, regex=None, minLength=None, maxLength=None):
    while(True):
        possibleStringFormat = enforceStringFormat(prompt, regex, minLength, maxLength)
        if 'Input' not in possibleStringFormat:
            break
        else:
            print(possibleStringFormat + ' Try again.')
    return possibleStringFormat

def strictEnforceBool(prompt):
    while(True):
        possibleBool = enforceBool(prompt)
        if isinstance(possibleBool, bool):
            break
        else:
            print(possibleBool + ' Try again.')
    return possibleBool

def strictEnforceComplex(prompt):
    while(True):
        possibleComplex = enforceComplex(prompt)
        if isinstance(possibleComplex, complex):
            break
        else:
            print(possibleComplex + ' Try again.')
    return possibleComplex