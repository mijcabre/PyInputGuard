# TODO: use random values instead of hardcoded ones
from PyInputGuard import *
import unittest
from unittest import mock

class TestEnforceFunctions(unittest.TestCase):

    def test_enforceInt(self):
        TEST_INT = 999
        TEST_FLOAT = 9.99
        TEST_STRING = 'asdf'
        TEST_BOOL = True
        TEST_COMPLEX = '1 + 2j'

        # test positive int
        # expect method to accept int
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceInt("Enter text: "), TEST_INT)

        # test negative int
        # expect method to accept int
        with mock.patch('builtins.input', return_value=str(TEST_INT * -1)):
            self.assertEqual(enforceInt("Enter text: "), TEST_INT * -1)

        # test positive float
        # expect method to fail to convert float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceInt("Enter text: "), f'Input "{TEST_FLOAT}" cannot be converted into an integer.')

        # test negative float
        # expect method to fail to convert float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT * -1)):
            self.assertEqual(enforceInt("Enter text: "), f'Input "{TEST_FLOAT * -1}" cannot be converted into an integer.')

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
        TEST_FLOAT = 9.99
        TEST_STRING = 'asdf'
        TEST_BOOL = True
        TEST_COMPLEX = '1 + 2j'

        # test positive int
        # expect method to accept int but convert to float
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceFloat("Enter text: "), float(TEST_INT))

        # test negative int
        # expect method to accept int but convert to float
        with mock.patch('builtins.input', return_value=str(TEST_INT * -1)):
            self.assertEqual(enforceFloat("Enter text: "), float(TEST_INT * -1))

        # test positive float
        # expect method to accept float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceFloat("Enter text: "), TEST_FLOAT)

        # test negative float
        # expect method to accept float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT * -1)):
            self.assertEqual(enforceFloat("Enter text: "), TEST_FLOAT * -1)

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
        TEST_BOOL = True
        TEST_COMPLEX = '1 + 2j'

        # test positive int
        # expect method to accept int as string
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceStringFormat("Enter text: "), str(TEST_INT))

        # test positive float
        # expect method to accept float as string
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceStringFormat("Enter text: "), str(TEST_FLOAT))

        # test string
        # without format
        # expect method to accept string
        with mock.patch('builtins.input', return_value=TEST_STRING):
            self.assertEqual(enforceStringFormat("Enter text: "), TEST_STRING)

        # test unformatted string
        # with required format
        # expect method to reject string
        with mock.patch('builtins.input', return_value=TEST_STRING):
            self.assertEqual(enforceStringFormat("Enter text: ", "hello[0-9]+"), f'Input "{TEST_STRING}" does not fit the specified format.')

        # test formatted string
        # with required format
        # expect method to accept string
        with mock.patch('builtins.input', return_value=TEST_STRING_FORMATTED):
            self.assertEqual(enforceStringFormat("Enter text: ", "hello[0-9]+"), TEST_STRING_FORMATTED)

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

        # test positive int
        # expect method to reject int as bool
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceBool("Enter text: "),  f'Input "{TEST_INT}" cannot be converted to a boolean.')

        # test positive float
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

        # test positive int
        # expect method to convert int
        with mock.patch('builtins.input', return_value=str(TEST_INT)):
            self.assertEqual(enforceComplex("Enter text: "), complex(TEST_INT))

        # test negative int
        # expect method to convert int
        with mock.patch('builtins.input', return_value=str(TEST_INT * -1)):
            self.assertEqual(enforceComplex("Enter text: "), complex(TEST_INT * -1))

        # test positive float
        # expect method to convert float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT)):
            self.assertEqual(enforceComplex("Enter text: "), complex(TEST_FLOAT+0j))

        # test negative float
        # expect method to convert float
        with mock.patch('builtins.input', return_value=str(TEST_FLOAT * -1)):
            self.assertEqual(enforceComplex("Enter text: "), complex(-1 * TEST_FLOAT+0j))

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