from PyInputGuard import *
import random
import string
import unittest
from unittest import mock

class TestEnforceFunctions(unittest.TestCase):

    def test_sizeCheck(self):
        TEST_INT = random.randint(1, 10)
        TEST_FLOAT = float(TEST_INT) + TEST_INT / 10
        TEST_STRING = random.choice(string.ascii_letters) * TEST_INT
        TEST_MIN_SIZE = TEST_INT - 1
        TEST_MAX_SIZE = TEST_INT + 1

        # test valid int
        # with min and max size correct
        # expect method to return int
        self.assertEqual(sizeCheck(TEST_INT, TEST_MIN_SIZE, TEST_MAX_SIZE), TEST_INT)

        # test invalid int
        # with min and max size correct
        # expect method to return error
        self.assertEqual(sizeCheck(TEST_INT * 1000, TEST_MIN_SIZE, TEST_MAX_SIZE), f'Input "{TEST_INT * 1000}" must be between "{TEST_MIN_SIZE - 1}" and "{TEST_MAX_SIZE + 1}"')

        # self.assertEqual(sizeCheck(TEST_INT * 1000, TEST_MIN_SIZE, TEST_MAX_SIZE), f'Input "{TEST_INT * 1000}" is too large. Input must be less than "{TEST_MAX_SIZE + 1}"')
        # test valid int
        # with min and max size flipped
        # expect method to return error
        self.assertEqual(sizeCheck(TEST_INT, TEST_MAX_SIZE, TEST_MIN_SIZE), f'minSize "{TEST_MAX_SIZE}" cannot be greater than or equal to maxSize "{TEST_MIN_SIZE}"')

        # test valid int
        # with min size
        # expect method to return int
        self.assertEqual(sizeCheck(TEST_INT, TEST_MIN_SIZE), TEST_INT)

        # test invalid int
        # with min size
        # expect method to return error
        self.assertEqual(sizeCheck(TEST_INT * 0, TEST_MIN_SIZE), f'Input "{TEST_INT * 0}" is too small. Input must be at least "{TEST_MIN_SIZE}"')

        # test valid int
        # with max size
        # expect method to return int
        self.assertEqual(sizeCheck(TEST_INT, None, TEST_MAX_SIZE), TEST_INT)

        # test invalid int
        # with max size
        # expect method to return error
        self.assertEqual(sizeCheck(TEST_INT * 1000, None, TEST_MAX_SIZE), f'Input "{TEST_INT * 1000}" is too large. Input must be less than "{TEST_MAX_SIZE + 1}"')

        # test valid float
        # with min and max size correct
        # expect method to return float
        self.assertEqual(sizeCheck(TEST_FLOAT, TEST_MIN_SIZE, TEST_MAX_SIZE), TEST_FLOAT)

        # test invalid float
        # with min and max size correct
        # expect method to return error
        self.assertEqual(sizeCheck(TEST_FLOAT * 1000, TEST_MIN_SIZE, TEST_MAX_SIZE), f'Input "{TEST_FLOAT * 1000}" must be between "{TEST_MIN_SIZE - 1}" and "{TEST_MAX_SIZE + 1}"')

        # test valid float
        # with min and max size flipped
        # expect method to return error
        self.assertEqual(sizeCheck(TEST_FLOAT, TEST_MAX_SIZE, TEST_MIN_SIZE), f'minSize "{TEST_MAX_SIZE}" cannot be greater than or equal to maxSize "{TEST_MIN_SIZE}"')

        # test valid float
        # with min size
        # expect method to return float
        self.assertEqual(sizeCheck(TEST_FLOAT, TEST_MIN_SIZE), TEST_FLOAT)

        # test invalid float
        # with min size
        # expect method to return error
        self.assertEqual(sizeCheck(TEST_FLOAT * 0, TEST_MIN_SIZE), f'Input "{TEST_FLOAT * 0}" is too small. Input must be at least "{TEST_MIN_SIZE}"')

        # test valid float
        # with max size
        # expect method to return float
        self.assertEqual(sizeCheck(TEST_FLOAT, None, TEST_MAX_SIZE), TEST_FLOAT)

        # test invalid float
        # with max size
        # expect method to return error
        self.assertEqual(sizeCheck(TEST_FLOAT * 1000, None, TEST_MAX_SIZE), f'Input "{TEST_FLOAT * 1000}" is too large. Input must be less than "{TEST_MAX_SIZE + 1}"')

        # test valid string
        # with min and max size correct
        # expect method to return string
        self.assertEqual(sizeCheck(TEST_STRING, TEST_MIN_SIZE, TEST_MAX_SIZE), TEST_STRING)

        # test invalid string
        # with min and max size correct
        # expect method to return error
        self.assertEqual(sizeCheck(TEST_STRING * 1000, TEST_MIN_SIZE, TEST_MAX_SIZE), f'Input "{TEST_STRING * 1000}" must be between "{TEST_MIN_SIZE - 1}" and "{TEST_MAX_SIZE + 1}" characters long')

        # test valid string
        # with min and max size flipped
        # expect method to return error
        self.assertEqual(sizeCheck(TEST_STRING, TEST_MAX_SIZE, TEST_MIN_SIZE), f'minSize "{TEST_MAX_SIZE}" cannot be greater than or equal to maxSize "{TEST_MIN_SIZE}" characters long')

        # test valid string
        # with min size
        # expect method to return string
        self.assertEqual(sizeCheck(TEST_STRING, TEST_MIN_SIZE), TEST_STRING)

        # test invalid string
        # with min size
        # expect method to return string
        self.assertEqual(sizeCheck(TEST_STRING * 0, TEST_MIN_SIZE), f'Input "{TEST_STRING * 0}" is too small. Input must be at least "{TEST_MIN_SIZE}" characters long')

        # test valid string
        # with max size
        # expect method to return string
        self.assertEqual(sizeCheck(TEST_STRING, None, TEST_MAX_SIZE), TEST_STRING)

        # test invalid string
        # with max size
        # expect method to return error
        self.assertEqual(sizeCheck(TEST_STRING * 1000, None, TEST_MAX_SIZE), f'Input "{TEST_STRING * 1000}" is too large. Input must be less than "{TEST_MAX_SIZE + 1}" characters long')


    def test_enforceInt(self):
        TEST_INT = random.randint(1, 10)
        TEST_MIN_SIZE = TEST_INT - 1
        TEST_MAX_SIZE = TEST_INT + 1
        TEST_FLOAT = float(TEST_INT) + TEST_INT / 10
        TEST_STRING = random.choice(string.ascii_letters) * TEST_INT
        TEST_BOOL = True
        TEST_COMPLEX = f'{TEST_INT} + {TEST_INT}j'

        # test int
        # expect method to accept int
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceInt("Enter text: "), TEST_INT)

        # test int
        # with max value
        # expect method to pass int
        with mock.patch('builtins.input', return_value=str(TEST_INT)[0]):
            self.assertEqual(enforceInt("Enter text: ", None, 10), int(str(TEST_INT)[0]))

        # test int
        # with max value
        # expect method to fail int
        with mock.patch('builtins.input', return_value=str(TEST_INT * 1000)):
            self.assertEqual(enforceInt("Enter text: ", None, TEST_MAX_SIZE), f'Input "{TEST_INT * 1000}" is too large. Input must be less than "{TEST_MAX_SIZE + 1}"')

        # test int
        # with min value
        # expect method to pass int
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceInt("Enter text: ", 1), TEST_INT)

        # test int
        # with min value
        # expect method to fail int
        with mock.patch('builtins.input', return_value=str(TEST_INT * -1)):
            self.assertEqual(enforceInt("Enter text: ", TEST_MIN_SIZE), f'Input "{TEST_INT * -1}" is too small. Input must be at least "{TEST_MIN_SIZE}"')

        # test int
        # with min and max value
        # expect method to pass int
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceInt("Enter text: ", TEST_MIN_SIZE, TEST_MAX_SIZE), TEST_INT)

        # test float
        # expect method to fail to convert float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceInt("Enter text: "), f'Input "{TEST_FLOAT}" cannot be converted into an integer')

        # test string
        # expect method to fail to convert string to int
        with mock.patch('builtins.input', return_value=TEST_STRING):
            self.assertEqual(enforceInt("Enter text: "), f'Input "{TEST_STRING}" cannot be converted into an integer')

        # test bool True
        # expect method to fail to convert bool to int
        with mock.patch('builtins.input', return_value=str(TEST_BOOL)):
            self.assertEqual(enforceInt("Enter text: "), f'Input "{TEST_BOOL}" cannot be converted into an integer')

        # test complex
        # expect method to reject complex
        with mock.patch('builtins.input', return_value=str(TEST_COMPLEX)):
            self.assertEqual(enforceInt("Enter text: "), f'Input "{TEST_COMPLEX}" cannot be converted into an integer')

    def test_enforceFloat(self):
        TEST_INT = random.randint(1, 10)
        TEST_FLOAT = float(TEST_INT) + TEST_INT / 10
        TEST_MIN_SIZE = TEST_INT - 1
        TEST_MAX_SIZE = TEST_INT + 1
        PRECISION = random.randint(1, 10)
        TEST_STRING = random.choice(string.ascii_letters) * TEST_INT
        TEST_BOOL = True
        TEST_COMPLEX = f'{TEST_INT} + {TEST_INT}j'

        # test int
        # expect method to accept int but convert to float
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceFloat("Enter text: "), float(TEST_INT))

        # test float
        # expect method to accept float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceFloat("Enter text: "), TEST_FLOAT)

        # test float
        # with precision
        # expect method to convert float to correct precision
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceFloat("Enter text: ", None, None, PRECISION), round(TEST_FLOAT, PRECISION))

        # test float
        # with min value
        # expect method to accept float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceFloat("Enter text: ", TEST_MIN_SIZE), TEST_FLOAT)

        # test float
        # with min value
        # expect method to reject float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT * -1)):
            self.assertEqual(enforceFloat("Enter text: ", TEST_MIN_SIZE), f'Input "{TEST_FLOAT * -1}" is too small. Input must be at least "{TEST_MIN_SIZE}"')

        # test float
        # with max value
        # expect method to accept float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceFloat("Enter text: ", None, TEST_MAX_SIZE), TEST_FLOAT)

        # test float
        # with max value
        # expect method to reject float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT * 1000)):
            self.assertEqual(enforceFloat("Enter text: ", None, TEST_MAX_SIZE), f'Input "{TEST_FLOAT * 1000}" is too large. Input must be less than "{TEST_MAX_SIZE + 1}"')

        # test float
        # with min and max value
        # expect method to accept float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceFloat("Enter text: ", TEST_MIN_SIZE, TEST_MAX_SIZE), TEST_FLOAT)

        # test float
        # with min and max value
        # expect method to reject float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT * -1)):
            self.assertEqual(enforceFloat("Enter text: ", TEST_MIN_SIZE, TEST_MAX_SIZE), f'Input "{TEST_FLOAT * -1}" must be between "{TEST_MIN_SIZE - 1}" and "{TEST_MAX_SIZE + 1}"')

        # test float
        # with min and max value flipped
        # expect method to reject float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceFloat("Enter text: ", TEST_MAX_SIZE, TEST_MIN_SIZE), f'minSize "{TEST_MAX_SIZE}" cannot be greater than or equal to maxSize "{TEST_MIN_SIZE}"')

        # test string
        # expect method to fail to convert string to float
        with mock.patch('builtins.input', return_value=TEST_STRING):
            self.assertEqual(enforceFloat("Enter text: "), f'Input "{TEST_STRING}" cannot be converted into a float')

        # test bool True
        # expect method to fail to convert bool to float
        with mock.patch('builtins.input', return_value=str(TEST_BOOL)):
            self.assertEqual(enforceFloat("Enter text: "), f'Input "{TEST_BOOL}" cannot be converted into a float')

        # test complex
        # expect method to reject complex
        with mock.patch('builtins.input', return_value=str(TEST_COMPLEX)):
            self.assertEqual(enforceFloat("Enter text: "), f'Input "{TEST_COMPLEX}" cannot be converted into a float')

    def test_enforceStringFormat(self):
        TEST_INT = random.randint(1, 10)
        TEST_FLOAT = float(TEST_INT) + TEST_INT / 10
        TEST_STRING = random.choice(string.ascii_letters) * TEST_INT
        TEST_STRING_FORMATTED = 'hello1'
        TEST_MIN_SIZE = TEST_INT - 1
        TEST_MAX_SIZE = TEST_INT + 1
        TEST_BOOL = True
        TEST_COMPLEX = f'{TEST_INT} + {TEST_INT}j'

        # test int
        # expect method to accept int as string
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceStringFormat("Enter text: "), str(TEST_INT))

        # test float
        # expect method to accept float as string
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceStringFormat("Enter text: "), str(TEST_FLOAT))

        # test string
        # without format
        # expect method to accept string
        with mock.patch('builtins.input', return_value=TEST_STRING):
            self.assertEqual(enforceStringFormat("Enter text: "), TEST_STRING)

        # test string
        # without format
        # with min length
        # expect method to accept string
        with mock.patch('builtins.input', return_value=TEST_STRING):
            self.assertEqual(enforceStringFormat("Enter text: ", None, TEST_MIN_SIZE), TEST_STRING)

        # test string
        # without format
        # with min length
        # expect method to reject string
        with mock.patch('builtins.input', return_value= TEST_STRING * 0):
            self.assertEqual(enforceStringFormat("Enter text: ", None, TEST_MIN_SIZE), f'Input "{TEST_STRING * 0}" is too small. Input must be at least "{TEST_MIN_SIZE}" characters long')

        # test string
        # without format
        # with max length
        # expect method to accept string
        with mock.patch('builtins.input', return_value=TEST_STRING):
            self.assertEqual(enforceStringFormat("Enter text: ", None, None, TEST_MAX_SIZE), TEST_STRING)

        # test string
        # without format
        # with max length
        # expect method to reject string
        with mock.patch('builtins.input', return_value=TEST_STRING * 1000):
            self.assertEqual(enforceStringFormat("Enter text: ", None, None, TEST_MAX_SIZE), f'Input "{TEST_STRING * 1000}" is too large. Input must be less than "{TEST_MAX_SIZE + 1}" characters long')

        # test string
        # without format
        # with min and max length
        # expect method to accept string
        with mock.patch('builtins.input', return_value=TEST_STRING):
            self.assertEqual(enforceStringFormat("Enter text: ", None, TEST_MIN_SIZE, TEST_MAX_SIZE), TEST_STRING)

        # test string
        # without format
        # with min and max length
        # expect method to reject string
        with mock.patch('builtins.input', return_value=TEST_STRING * 1000):
            self.assertEqual(enforceStringFormat("Enter text: ", None, TEST_MIN_SIZE, TEST_MAX_SIZE), f'Input "{TEST_STRING * 1000}" must be between "{TEST_MIN_SIZE - 1}" and "{TEST_MAX_SIZE + 1}" characters long')

        # test string
        # without format
        # with min and max length flipped
        # expect method to reject string
        with mock.patch('builtins.input', return_value=TEST_STRING * 1000):
            self.assertEqual(enforceStringFormat("Enter text: ", None, TEST_MAX_SIZE, TEST_MIN_SIZE), f'minSize "{TEST_MAX_SIZE}" cannot be greater than or equal to maxSize "{TEST_MIN_SIZE}" characters long')

        # test formatted string
        # with required format
        # expect method to accept string
        with mock.patch('builtins.input', return_value=TEST_STRING_FORMATTED):
            self.assertEqual(enforceStringFormat("Enter text: ", "hello[0-9]+"), TEST_STRING_FORMATTED)

        # test string
        # with required format
        # expect method to reject string
        with mock.patch('builtins.input', return_value=TEST_STRING):
            self.assertEqual(enforceStringFormat("Enter text: ", "hello[0-9]+"), f'Input "{TEST_STRING}" does not fit the specified regular expression')

        # test bool True
        # expect method to accept bool as string
        with mock.patch('builtins.input', return_value=str(TEST_BOOL)):
            self.assertEqual(enforceStringFormat("Enter text: "), str(TEST_BOOL))

        # test complex
        # expect method to accept complex as string
        with mock.patch('builtins.input', return_value=str(TEST_COMPLEX)):
            self.assertEqual(enforceStringFormat("Enter text: "), str(TEST_COMPLEX))

    def test_enforceBool(self):
        TEST_INT = random.randint(1, 10)
        TEST_FLOAT = float(TEST_INT) + TEST_INT / 10
        TEST_STRING = random.choice(string.ascii_letters) * TEST_INT
        TEST_BOOL_TRUE = True
        TEST_BOOL_FALSE = False
        TEST_BOOL_YES = 'yes'
        TEST_BOOL_NO = 'no'
        TEST_COMPLEX = f'{TEST_INT} + {TEST_INT}j'

        # test int
        # expect method to reject int as bool
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceBool("Enter text: "),  f'Input "{TEST_INT}" cannot be converted to a boolean')

        # test float
        # expect method to reject float as bool
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceBool("Enter text: "),  f'Input "{TEST_FLOAT}" cannot be converted to a boolean')

        # test string
        # without format
        # expect method to reject string as bool
        with mock.patch('builtins.input', return_value=TEST_STRING):
            self.assertEqual(enforceBool("Enter text: "),  f'Input "{TEST_STRING}" cannot be converted to a boolean')

        # test bool True
        # expect method to accept bool True
        with mock.patch('builtins.input', return_value=str(TEST_BOOL_TRUE)):
            self.assertEqual(enforceBool("Enter text: "), TEST_BOOL_TRUE)

        # test bool false
        # expect method to accept bool false
        with mock.patch('builtins.input', return_value=str(TEST_BOOL_FALSE)):
            self.assertEqual(enforceBool("Enter text: "), TEST_BOOL_FALSE)

        # test bool True
        # expect method to accept bool True
        with mock.patch('builtins.input', return_value=str(TEST_BOOL_YES)):
            self.assertEqual(enforceBool("Enter text: "), TEST_BOOL_TRUE)

        # test bool false
        # expect method to accept bool false
        with mock.patch('builtins.input', return_value=str(TEST_BOOL_NO)):
            self.assertEqual(enforceBool("Enter text: "), TEST_BOOL_FALSE)

        # test complex
        # expect method to reject complex
        with mock.patch('builtins.input', return_value=str(TEST_COMPLEX)):
            self.assertEqual(enforceBool("Enter text: "), f'Input "{TEST_COMPLEX}" cannot be converted to a boolean')


    def test_enforceComplex(self):
        TEST_INT = random.randint(1, 10)
        TEST_FLOAT = float(TEST_INT) + TEST_INT / 10
        TEST_STRING = random.choice(string.ascii_letters) * TEST_INT
        TEST_BOOL = True
        TEST_COMPLEX = f'{TEST_INT} + {TEST_INT}j'

        # test int
        # expect method to convert int
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceComplex("Enter text: "), complex(TEST_INT))

        # test float
        # expect method to convert float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceComplex("Enter text: "), complex(TEST_FLOAT+0j))

        # test string
        # expect method to fail to convert string to complex
        with mock.patch('builtins.input', return_value=TEST_STRING):
            self.assertEqual(enforceComplex("Enter text: "), f'Input "{TEST_STRING}" cannot be converted into a complex number')

        # test bool True
        # expect method to fail to convert bool to int
        with mock.patch('builtins.input', return_value=str(TEST_BOOL)):
            self.assertEqual(enforceComplex("Enter text: "), f'Input "{TEST_BOOL}" cannot be converted into a complex number')

        # test complex
        # expect method to convert to complex
        with mock.patch('builtins.input', return_value=str(TEST_COMPLEX)):
            self.assertEqual(enforceComplex("Enter text:"), complex(TEST_COMPLEX.replace(" ", "")))

    def test_strictEnforceInt(self):
        TEST_INT = random.randint(1, 10)
        TEST_MIN_SIZE = TEST_INT - 1
        TEST_MAX_SIZE = TEST_INT + 1

        # test int
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(strictEnforceInt("Enter text: "), TEST_INT)

        # test int
        # with min value
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(strictEnforceInt("Enter text: ", TEST_MIN_SIZE), TEST_INT)

        # test int
        # with max value
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(strictEnforceInt("Enter text: ", None, TEST_MAX_SIZE), TEST_INT)

        # test int
        # with min and max value
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(strictEnforceInt("Enter text: ", TEST_MIN_SIZE, TEST_MAX_SIZE), TEST_INT)

    def test_strictEnforceFloat(self):
        TEST_INT = random.randint(1, 10)
        TEST_FLOAT = float(TEST_INT) + TEST_INT / 10
        TEST_MIN_SIZE = TEST_INT - 1
        TEST_MAX_SIZE = TEST_INT + 1
        PRECISION = random.randint(1, 10)

        # test float
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(strictEnforceFloat("Enter text: "), TEST_FLOAT)

        # test float
        # with min value
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(strictEnforceFloat("Enter text: ", TEST_MIN_SIZE), TEST_FLOAT)

        # test float
        # with max value
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(strictEnforceFloat("Enter text: ", None, TEST_MAX_SIZE), TEST_FLOAT)

        # test float
        # with min and max value
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(strictEnforceFloat("Enter text: ", TEST_MIN_SIZE, TEST_MAX_SIZE), TEST_FLOAT)

        # test float
        # with precision
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(strictEnforceFloat("Enter text: ", None, None, PRECISION), round(TEST_FLOAT, PRECISION))

    def test_strictEnforceStringFormat(self):
        TEST_STRING = 'hello3'
        TEST_REGEX = 'hello[1-9]+'
        TEST_MIN_SIZE = len(TEST_STRING) - 1
        TEST_MAX_SIZE = len(TEST_STRING) + 1

        # test string
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_STRING)):
            self.assertEqual(strictEnforceStringFormat("Enter text: "), TEST_STRING)

        # test string
        # with regex
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_STRING)):
            self.assertEqual(strictEnforceStringFormat("Enter text: ", TEST_REGEX), TEST_STRING)

        # test string
        # with min length
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_STRING)):
            self.assertEqual(strictEnforceStringFormat("Enter text: ", None, TEST_MIN_SIZE), TEST_STRING)

        # test string
        # with max length
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_STRING)):
            self.assertEqual(strictEnforceStringFormat("Enter text: ", None, None, TEST_MAX_SIZE), TEST_STRING)

        # test string
        # with min and max length
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_STRING)):
            self.assertEqual(strictEnforceStringFormat("Enter text: ", None, TEST_MIN_SIZE, TEST_MAX_SIZE), TEST_STRING)

        # test string
        # with min, max, regex
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_STRING)):
            self.assertEqual(strictEnforceStringFormat("Enter text: ", TEST_REGEX, TEST_MIN_SIZE, TEST_MAX_SIZE), TEST_STRING)

    def test_strictEnforceBool(self):
        TEST_TRUE = "true"
        TEST_FALSE = "false"

        # test bool
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_TRUE)):
            self.assertEqual(strictEnforceBool("Enter text: "), True)

        # test bool
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_FALSE)):
            self.assertEqual(strictEnforceBool("Enter text: "), False)

    def test_strictEnforceComplex(self):
        TEST_INT = random.randint(1, 10)
        TEST_COMPLEX = f'{TEST_INT} + {TEST_INT}j'
        RESULT_COMPLEX = complex(TEST_COMPLEX.replace(' ', ''))

        # test complex
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_COMPLEX)):
            self.assertEqual(strictEnforceComplex("Enter text: "), RESULT_COMPLEX)

if __name__ == "__main__":
    unittest.main()