# TODO: add checking data directly(not using a prompt, example: x = enforceInt(someData))
# TODO: add length/size checking to enforceInt, enforceFloat, enforceString, ...?
# TODO: add precision checking to enforceFloat
# TODO: add enforceBool
# TODO: add enforceComplex
# TODO: add enforceByte
# TODO: add enforceList
# TODO: add enforceTuple
# TODO: add enforceSet
# TODO: add enforceDictionary


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
            return f'Input "{testInput}" oes not fit the specified format'
    else:
        return testInput
