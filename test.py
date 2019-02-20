# TODO: use random values instead of hardcoded ones

from PyInputGuard import *
import unittest
from unittest import mock

class TestEnforceFunctions(unittest.TestCase):

    def test_sizeCheck(self):
        TEST_INT = 9
        TEST_FLOAT = 9.99
        TEST_STRING = 'asdf'
        TEST_MIN_SIZE = 2
        TEST_MAX_SIZE = 10

        # test valid int
        # with min and max size correct
        # expect method to return int
        self.assertEqual(sizeCheck(TEST_INT, TEST_MIN_SIZE, TEST_MAX_SIZE), TEST_INT)

        # test invalid int
        # with min and max size correct
        # expect method to return error
        self.assertEqual(sizeCheck(TEST_INT * 1000, TEST_MIN_SIZE, TEST_MAX_SIZE), f'Input "{TEST_INT * 1000}" must be between "{TEST_MIN_SIZE - 1}" and "{TEST_MAX_SIZE + 1}"')

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
        TEST_INT = 999
        MIN_VALUE = 1
        MAX_VALUE = 10
        TEST_FLOAT = 9.99
        TEST_STRING = 'asdf'
        TEST_BOOL = True
        TEST_COMPLEX = '1 + 2j'

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
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceInt("Enter text: ", None, 10), f'Input "{TEST_INT}" is too large. Input must be less than "{MAX_VALUE + 1}"')

        # test int
        # with min value
        # expect method to pass int
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceInt("Enter text: ", 1), TEST_INT)

        # test int
        # with min value
        # expect method to fail int
        with mock.patch('builtins.input', return_value=str(TEST_INT * -1)):
            self.assertEqual(enforceInt("Enter text: ", 1), f'Input "{TEST_INT * -1}" is too small. Input must be at least "{MIN_VALUE}"')

        # test int
        # with min and max value
        # expect method to pass int
        with mock.patch('builtins.input', return_value=str(TEST_INT)[0]):
            self.assertEqual(enforceInt("Enter text: ", 1, 10), int(str(TEST_INT)[0]))

        # test int
        # with min and max value
        # expect method to fail int
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceInt("Enter text: ", 1, 10), f'Input "{TEST_INT}" must be between "{MIN_VALUE - 1}" and "{MAX_VALUE + 1}"')

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
        TEST_INT = 999
        TEST_FLOAT = 9.999
        MIN_VALUE = 1
        MAX_VALUE = 10
        PRECISION = 2
        TEST_STRING = 'asdf'
        TEST_BOOL = True
        TEST_COMPLEX = '1 + 2j'

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
            self.assertEqual(enforceFloat("Enter text: ", MIN_VALUE), TEST_FLOAT)

        # test float
        # with min value
        # expect method to reject float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT * -1)):
            self.assertEqual(enforceFloat("Enter text: ", MIN_VALUE), f'Input "{TEST_FLOAT * -1}" is too small. Input must be at least "{MIN_VALUE}"')

        # test float
        # with max value
        # expect method to accept float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceFloat("Enter text: ", None, MAX_VALUE), TEST_FLOAT)

        # test float
        # with max value
        # expect method to reject float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT * 10)):
            self.assertEqual(enforceFloat("Enter text: ", None, MAX_VALUE), f'Input "{TEST_FLOAT * 10}" is too large. Input must be less than "{MAX_VALUE + 1}"')

        # test float
        # with min and max value
        # expect method to accept float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceFloat("Enter text: ", MIN_VALUE, MAX_VALUE), TEST_FLOAT)

        # test float
        # with min and max value
        # expect method to reject float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT * -1)):
            self.assertEqual(enforceFloat("Enter text: ", MIN_VALUE, MAX_VALUE), f'Input "{TEST_FLOAT * -1}" must be between "{MIN_VALUE - 1}" and "{MAX_VALUE + 1}"')

        # test float
        # with min and max value flipped
        # expect method to reject float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceFloat("Enter text: ", MAX_VALUE, MIN_VALUE), f'minSize "{MAX_VALUE}" cannot be greater than or equal to maxSize "{MIN_VALUE}"')

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
        TEST_INT = 999
        TEST_FLOAT = 9.99
        TEST_STRING = 'asdf'
        TEST_STRING_FORMATTED = 'hello1'
        MIN_LENGTH = 4
        MAX_LENGTH = 10
        TEST_BOOL = True
        TEST_COMPLEX = '1 + 2j'

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
            self.assertEqual(enforceStringFormat("Enter text: ", None, MIN_LENGTH), TEST_STRING)

        # test string
        # without format
        # with min length
        # expect method to reject string
        with mock.patch('builtins.input', return_value=TEST_STRING[:2]):
            self.assertEqual(enforceStringFormat("Enter text: ", None, MIN_LENGTH), f'Input "{TEST_STRING[:2]}" is too small. Input must be at least "{MIN_LENGTH}" characters long')

        # test string
        # without format
        # with max length
        # expect method to accept string
        with mock.patch('builtins.input', return_value=TEST_STRING):
            self.assertEqual(enforceStringFormat("Enter text: ", None, None, MAX_LENGTH), TEST_STRING)

        # test string
        # without format
        # with max length
        # expect method to reject string
        with mock.patch('builtins.input', return_value=TEST_STRING * 10):
            self.assertEqual(enforceStringFormat("Enter text: ", None, None, MAX_LENGTH), f'Input "{TEST_STRING * 10}" is too large. Input must be less than "{MAX_LENGTH + 1}" characters long')

        # test string
        # without format
        # with min and max length
        # expect method to accept string
        with mock.patch('builtins.input', return_value=TEST_STRING):
            self.assertEqual(enforceStringFormat("Enter text: ", None, MIN_LENGTH, MAX_LENGTH), TEST_STRING)

        # test string
        # without format
        # with min and max length
        # expect method to reject string
        with mock.patch('builtins.input', return_value=TEST_STRING * 10):
            self.assertEqual(enforceStringFormat("Enter text: ", None, MIN_LENGTH, MAX_LENGTH), f'Input "{TEST_STRING * 10}" must be between "{MIN_LENGTH - 1}" and "{MAX_LENGTH + 1}" characters long')

        # test string
        # without format
        # with min and max length flipped
        # expect method to reject string
        with mock.patch('builtins.input', return_value=TEST_STRING * 10):
            self.assertEqual(enforceStringFormat("Enter text: ", None, MAX_LENGTH, MIN_LENGTH), f'minSize "{MAX_LENGTH}" cannot be greater than or equal to maxSize "{MIN_LENGTH}" characters long')

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
        TEST_INT = 999
        TEST_FLOAT = 9.99
        TEST_STRING = 'asdf'
        TEST_BOOL_TRUE = True
        TEST_BOOL_FALSE = False
        TEST_BOOL_YES = 'yes'
        TEST_BOOL_NO = 'no'
        TEST_COMPLEX = '1 + 2j'

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
        TEST_INT = 999
        TEST_FLOAT = 9.99
        TEST_STRING = 'asdf'
        TEST_BOOL = True
        TEST_COMPLEX = "(1 + 2j)"

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
        TEST_INT = 999
        MIN_VALUE = 500
        MAX_VALUE = 1000
        # test int
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(strictEnforceInt("Enter text: "), TEST_INT)

        # test int
        # with min value
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(strictEnforceInt("Enter text: ", MIN_VALUE), TEST_INT)

        # test int
        # with max value
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(strictEnforceInt("Enter text: ", None, MAX_VALUE), TEST_INT)

        # test int
        # with min and max value
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(strictEnforceInt("Enter text: ", MIN_VALUE, MAX_VALUE), TEST_INT)

    def test_strictEnforceFloat(self):
        TEST_FLOAT = 9.999
        MIN_VALUE = 1
        MAX_VALUE = 10
        PRECISION = 2

        # test float
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(strictEnforceFloat("Enter text: "), TEST_FLOAT)

        # test float
        # with min value
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(strictEnforceFloat("Enter text: ", MIN_VALUE), TEST_FLOAT)

        # test float
        # with max value
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(strictEnforceFloat("Enter text: ", None, MAX_VALUE), TEST_FLOAT)

        # test float
        # with min and max value
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(strictEnforceFloat("Enter text: ", MIN_VALUE, MAX_VALUE), TEST_FLOAT)

        # test float
        # with precision
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(strictEnforceFloat("Enter text: ", None, None, PRECISION), round(TEST_FLOAT, PRECISION))

    def test_strictEnforceStringFormat(self):
        TEST_STRING = 'hello3'
        TEST_REGEX = 'hello[1-9]+'
        MIN_LENGTH = 2
        MAX_LENGTH = 10

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
            self.assertEqual(strictEnforceStringFormat("Enter text: ", None, MIN_LENGTH), TEST_STRING)

        # test string
        # with max length
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_STRING)):
            self.assertEqual(strictEnforceStringFormat("Enter text: ", None, None, MAX_LENGTH), TEST_STRING)

        # test string
        # with min and max length
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_STRING)):
            self.assertEqual(strictEnforceStringFormat("Enter text: ", None, MIN_LENGTH, MAX_LENGTH), TEST_STRING)

        # test string
        # with min, max, regex
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_STRING)):
            self.assertEqual(strictEnforceStringFormat("Enter text: ", TEST_REGEX, MIN_LENGTH, MAX_LENGTH), TEST_STRING)

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
        TEST_COMPLEX = '( 4 + 5j)'
        RESULT_COMPLEX = complex(4+5j)

        # test complex
        # expect accept
        with mock.patch('builtins.input', return_value=str(TEST_COMPLEX)):
            self.assertEqual(strictEnforceComplex("Enter text: "), RESULT_COMPLEX)

if __name__ == "__main__":
    unittest.main()