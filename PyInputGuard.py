# TODO: add documentation in README

import re


def sizeCheck(testInput, minSize = None, maxSize = None):
    """
    Helper method for enforceInt, enforceFloat, enforceStringFormat
    Args:
        testInput: input to test for size
        minSize: minimum size for testInput
        maxSize: maximum size for testInput

    Returns:
        Error message if invalid testInput
        Value if valid testInput
    """
    if isinstance(testInput, str):
        testInputSize = len(testInput)
    else:
        testInputSize = testInput

    if minSize and maxSize or minSize == 0 and maxSize == 0:
        if minSize >= maxSize:
            return_str = f'minSize "{minSize}" cannot be greater than or equal to maxSize "{maxSize}"'
            if isinstance(testInput, str):
                return_str += ' characters long'
            return return_str
        elif testInputSize >= minSize and testInputSize <= maxSize:
            return testInput
        else:
            return_str = f'Input "{testInput}" must be between "{minSize - 1}" and "{maxSize + 1}"'
            if isinstance(testInput, str):
                return_str += ' characters long'
            return return_str
    elif minSize or minSize == 0:
        if testInputSize >= minSize:
            return testInput
        else:
            return_str = f'Input "{testInput}" is too small. Input must be at least "{minSize}"'
            if isinstance(testInput, str):
                return_str += ' characters long'
            return return_str
    elif maxSize or maxSize == 0:
        if testInputSize <= maxSize:
            return testInput
        else:
            return_str = f'Input "{testInput}" is too large. Input must be less than "{maxSize + 1}"'
            if isinstance(testInput, str):
                return_str += ' characters long'
            return return_str
    else:
        return testInput

def enforceInt(prompt, minValue = None, maxValue = None):
    """
    Enforces an integer at a prompt
    Args:
        prompt: String for user input prompt
        minValue: minimum valid int value
        maxValue: maximum valid int value
    Returns:
        Error string if invalid
        Int if valid
    """
    testInput = input(prompt)
    try:
        testInput = int(testInput)
        return sizeCheck(testInput, minValue, maxValue)
    except:
        return f'Input "{testInput}" cannot be converted into an integer'

def enforceFloat(prompt, minValue = None, maxValue = None, precision = None):
    """
    Enforces a float at a prompt
    Args:
        prompt: String for user input prompt
        minValue: minimum valid float value
        maxValue: maximum valid float value
        precision: desired precision of float
    Returns:
        Error string if invalid
        Float if valid
    """
    testInput = input(prompt)
    try:
        testInput = float(testInput)
        if precision != None:
            testInput = round(testInput, precision)
        return sizeCheck(testInput, minValue, maxValue)
    except:
        return f'Input "{testInput}" cannot be converted into a float'

def enforceStringFormat(prompt,  regex = None, minLength = None, maxLength = None):
    """
    Enforces a string at a prompt
    Args:
        prompt: String for user input prompt
        regex: regular expression the string should conform to
        minLength: minimum valid string length
        maxValue: maximum valid string length
    Returns:
        Error string if invalid
        Test input if valid
    """
    testInput = input(prompt)
    if regex != None:
        pattern = re.compile(regex)
        if bool(pattern.match(testInput)):
            return testInput
        else:
           return f'Input "{testInput}" does not fit the specified regular expression'
    else:
        return sizeCheck(testInput, minLength, maxLength)

def enforceBool(prompt):
    """
    Enforces a boolean/YesNo value at a prompt
    Args:
        prompt: String for user input prompt
    Returns:
        Error string if invalid
        Test input if valid
    """
    testInput = input(prompt)
    if testInput in ['true', 'True', 'TRUE', 'Yes', 'yes', 'YES']:
        return True
    elif testInput in ['false', 'False', 'FALSE', 'No', 'no', 'NO']:
        return False
    else:
        return f'Input "{testInput}" cannot be converted to a boolean'

def enforceComplex(prompt):
    """
    Enforces a complex number at a prompt
    Args:
        prompt: String for user input prompt
    Returns:
        Error string if invalid
        Test input if valid
    """
    testInput = input(prompt)
    testInput = testInput.replace(" ", "")
    try:
        return complex(testInput)
    except:
        return f'Input "{testInput}" cannot be converted into a complex number'

def strictEnforceInt(prompt, minValue = None, maxValue = None):
    """
    Enforces an integer at a prompt. Loops until valid input given
    Args:
        prompt: String for user input prompt
        minValue: minimum valid int value
        maxValue: maximum valid int value
    Returns:
        Error string if invalid
        Int if valid
    """
    while(True):
        possibleInt = enforceInt(prompt, minValue, maxValue)
        if isinstance(possibleInt, int):
            break
        else:
            print(possibleInt + ' Try again')
    return possibleInt

def strictEnforceFloat(prompt, minValue = None, maxValue = None, precision = None):
    """
    Enforces a float at a prompt. Loops until valid input given
    Args:
        prompt: String for user input prompt
        minValue: minimum valid float value
        maxValue: maximum valid float value
        precision: desired precision of float
    Returns:
        Error string if invalid
        Float if valid
    """
    while(True):
        possibleFloat = enforceFloat(prompt, minValue, maxValue, precision)
        if isinstance(possibleFloat, float):
            break
        else:
            print(possibleFloat + ' Try again')
    return possibleFloat

def strictEnforceStringFormat(prompt, regex = None, minLength = None, maxLength = None):
    """
    Enforces a string at a prompt. Loops until valid input given
    Args:
        prompt: String for user input prompt
        regex: regular expression the string should conform to
        minLength: minimum valid string length
        maxValue: maximum valid string length
    Returns:
        Error string if invalid
        Test input if valid
    """
    while(True):
        possibleStringFormat = enforceStringFormat(prompt, regex, minLength, maxLength)
        if 'Input' not in possibleStringFormat:
            break
        else:
            print(possibleStringFormat + ' Try again')
    return possibleStringFormat

def strictEnforceBool(prompt):
    """
    Enforces a boolean/YesNo value at a prompt. Loops until valid input given
    Args:
        prompt: String for user input prompt
    Returns:
        Error string if invalid
        Test input if valid
    """
    while(True):
        possibleBool = enforceBool(prompt)
        if isinstance(possibleBool, bool):
            break
        else:
            print(possibleBool + ' Try again')
    return possibleBool

def strictEnforceComplex(prompt):
    """
    Enforces a complex number at a prompt. Loops until valid input given
    Args:
        prompt: String for user input prompt
    Returns:
        Error string if invalid
        Test input if valid
    """
    while(True):
        possibleComplex = enforceComplex(prompt)
        if isinstance(possibleComplex, complex):
            break
        else:
            print(possibleComplex + ' Try again')
    return possibleComplex
