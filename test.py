# TODO: use random values instead of hardcoded ones
from PyInputGuard import *
import unittest
from unittest import mock

class TestEnforceFunctions(unittest.TestCase):

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
            self.assertEqual(enforceInt("Enter text: ", None, 10), f'Input "{TEST_INT}" is too large. Input must be less than {MAX_VALUE + 1}.')

        # test int
        # with min value
        # expect method to pass int
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceInt("Enter text: ", 1), TEST_INT)

        # test int
        # with min value
        # expect method to fail int
        with mock.patch('builtins.input', return_value=str(TEST_INT * -1)):
            self.assertEqual(enforceInt("Enter text: ", 1), f'Input "{TEST_INT * -1}" is too small. Input must be at least {MIN_VALUE}.')

        # test int
        # with min and max value
        # expect method to pass int
        with mock.patch('builtins.input', return_value=str(TEST_INT)[0]):
            self.assertEqual(enforceInt("Enter text: ", 1, 10), int(str(TEST_INT)[0]))

        # test int
        # with min and max value
        # expect method to fail int
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceInt("Enter text: ", 1, 10), f'Input "{TEST_INT}" must be between {MIN_VALUE - 1} and {MAX_VALUE + 1}.')

        # test float
        # expect method to fail to convert float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceInt("Enter text: "), f'Input "{TEST_FLOAT}" cannot be converted into an integer.')

        # test string
        # expect method to fail to convert string to int
        with mock.patch('builtins.input', return_value=TEST_STRING):
            self.assertEqual(enforceInt("Enter text: "), f'Input "{TEST_STRING}" cannot be converted into an integer.')

        # test bool True
        # expect method to fail to convert bool to int
        with mock.patch('builtins.input', return_value=str(TEST_BOOL)):
            self.assertEqual(enforceInt("Enter text: "), f'Input "{TEST_BOOL}" cannot be converted into an integer.')

        # test complex
        # expect method to reject complex
        with mock.patch('builtins.input', return_value=str(TEST_COMPLEX)):
            self.assertEqual(enforceInt("Enter text: "), f'Input "{TEST_COMPLEX}" cannot be converted into an integer.')

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
            self.assertEqual(enforceFloat("Enter text: ", None, None, PRECISION), 9.99)

        # test float
        # with min value
        # expect method to accept float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceFloat("Enter text: ", MIN_VALUE), TEST_FLOAT)

        # test float
        # with min value
        # expect method to reject float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT * -1)):
            self.assertEqual(enforceFloat("Enter text: ", MIN_VALUE), f'Input "{TEST_FLOAT * -1}" is too small. Input must be at least {MIN_VALUE}.')

        # test float
        # with max value
        # expect method to accept float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceFloat("Enter text: ", None, MAX_VALUE), TEST_FLOAT)

        # test float
        # with max value
        # expect method to reject float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT * 10)):
            self.assertEqual(enforceFloat("Enter text: ", None, MAX_VALUE), f'Input "{TEST_FLOAT * 10}" is too large. Input must be less than {MAX_VALUE + 1}.')

        # test float
        # with min and max value
        # expect method to accept float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceFloat("Enter text: ", MIN_VALUE, MAX_VALUE), TEST_FLOAT)

        # test float
        # with min and max value
        # expect method to reject float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT * -1)):
            self.assertEqual(enforceFloat("Enter text: ", MIN_VALUE, MAX_VALUE), f'Input "{TEST_FLOAT * -1}" must be between {MIN_VALUE - 1} and {MAX_VALUE + 1}.')

        # test string
        # expect method to fail to convert string to float
        with mock.patch('builtins.input', return_value=TEST_STRING):
            self.assertEqual(enforceFloat("Enter text: "), f'Input "{TEST_STRING}" cannot be converted into a float.')

        # test bool True
        # expect method to fail to convert bool to float
        with mock.patch('builtins.input', return_value=str(TEST_BOOL)):
            self.assertEqual(enforceFloat("Enter text: "), f'Input "{TEST_BOOL}" cannot be converted into a float.')

        # test complex
        # expect method to reject complex
        with mock.patch('builtins.input', return_value=str(TEST_COMPLEX)):
            self.assertEqual(enforceFloat("Enter text: "), f'Input "{TEST_COMPLEX}" cannot be converted into a float.')

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
            self.assertEqual(enforceStringFormat("Enter text: ", None, MIN_LENGTH), f'Input "{TEST_STRING[:2]}" is too small. Input must be at least {MIN_LENGTH} characters long.')

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
            self.assertEqual(enforceStringFormat("Enter text: ", None, None, MAX_LENGTH), f'Input "{TEST_STRING * 10}" is too large. Input must be less than {MAX_LENGTH + 1} characters long.')

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
            self.assertEqual(enforceStringFormat("Enter text: ", None, MIN_LENGTH, MAX_LENGTH), f'Input "{TEST_STRING * 10}" must be between {MIN_LENGTH - 1} and {MAX_LENGTH + 1} characters long.')

        # test formatted string
        # with required format
        # expect method to accept string
        with mock.patch('builtins.input', return_value=TEST_STRING_FORMATTED):
            self.assertEqual(enforceStringFormat("Enter text: ", "hello[0-9]+"), TEST_STRING_FORMATTED)

        # test string
        # with required format
        # expect method to reject string
        with mock.patch('builtins.input', return_value=TEST_STRING):
            self.assertEqual(enforceStringFormat("Enter text: ", "hello[0-9]+"), f'Input "{TEST_STRING}" does not fit the specified format.')

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
        TEST_COMPLEX = '1 + 2j'

        # test int
        # expect method to reject int as bool
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceBool("Enter text: "),  f'Input "{TEST_INT}" cannot be converted to a boolean.')

        # test float
        # expect method to reject float as bool
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceBool("Enter text: "),  f'Input "{TEST_FLOAT}" cannot be converted to a boolean.')

        # test string
        # without format
        # expect method to reject string as bool
        with mock.patch('builtins.input', return_value=TEST_STRING):
            self.assertEqual(enforceBool("Enter text: "),  f'Input "{TEST_STRING}" cannot be converted to a boolean.')

        # test bool True
        # expect method to accept bool True
        with mock.patch('builtins.input', return_value=str(TEST_BOOL_TRUE)):
            self.assertEqual(enforceBool("Enter text: "), TEST_BOOL_TRUE)

        # test bool True
        # expect method to accept bool True
        with mock.patch('builtins.input', return_value=str(TEST_BOOL_FALSE)):
            self.assertEqual(enforceBool("Enter text: "), TEST_BOOL_FALSE)

        # test complex
        # expect method to reject complex
        with mock.patch('builtins.input', return_value=str(TEST_COMPLEX)):
            self.assertEqual(enforceBool("Enter text: "), f'Input "{TEST_COMPLEX}" cannot be converted to a boolean.')


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
            self.assertEqual(enforceComplex("Enter text: "), f'Input "{TEST_STRING}" cannot be converted into a complex number.')

        # test bool True
        # expect method to fail to convert bool to int
        with mock.patch('builtins.input', return_value=str(TEST_BOOL)):
            self.assertEqual(enforceComplex("Enter text: "), f'Input "{TEST_BOOL}" cannot be converted into a complex number.')

        # test complex
        # expect method to convert to complex
        with mock.patch('builtins.input', return_value=str(TEST_COMPLEX)):
            self.assertEqual(enforceComplex("Enter text:"), complex(TEST_COMPLEX.replace(" ", "")))

if __name__ == "__main__":
    unittest.main()