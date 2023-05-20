import numpy as np
from unittest import TestCase

import exercise


class TestFunctionAsArgument(TestCase):
    def test_calculate_keys_length(self):
        """
        Test that the calculate function returns a dictionary with the same number of keys as the number of functions
        """
        for i in range(1, len(exercise.FUNCS_NAMES)):
            expected_keys_length = i
            funcs = [getattr(np, func_name) for func_name in exercise.FUNCS_NAMES[:i]]
            actual_keys_length = len(exercise.calculate([1, 2], *funcs).keys())
            self.assertEqual(
                expected_keys_length,
                actual_keys_length,
                msg="calculate function should return a dictionary with the same "
                "number of keys as the number of functions passed to it",
            )

    def test_calculate_keys(self):
        """
        Test that the calculate function returns a dictionary with the same keys as the function names passed to it
        """
        expected_keys = ["sum", "amin", "amax"]
        actual_keys = exercise.calculate([1, 2], np.sum, np.min, np.max).keys()
        self.assertListEqual(
            expected_keys,
            list(actual_keys),
            msg="calculate function should return a dictionary with function names as keys",
        )

    def test_calculate_values(self):
        """
        Test that the calculate function returns a dictionary with the correct values
        """
        expected_values = [3, 1, 2]
        actual_values = exercise.calculate([1, 2], np.sum, np.min, np.max).values()
        self.assertListEqual(
            expected_values,
            list(actual_values),
            msg="calculate function should return a dictionary with function call as values",
        )

    def test_main_keys_length(self):
        """
        Test that the main function returns a dictionary with the same number of keys as the number of functions
        """
        expected_keys_length = len(exercise.FUNCS_NAMES)
        actual_keys_length = len(exercise.main().keys())

        self.assertEqual(
            expected_keys_length,
            actual_keys_length,
            msg="The length of the dictionary should be the same as the number of function names in FUNCS_NAMES",
        )

    def test_main_keys(self):
        """
        Test that the main function returns a dictionary with the same keys as the function names in FUNCS_NAMES
        """
        expected_keys = exercise.FUNCS_NAMES
        actual_keys = list(exercise.main().keys())

        self.assertListEqual(expected_keys, actual_keys)

    def test_main_selected_values(self):
        """
        Test that the main function returns a dictionary with the correct values for the selected functions
        """
        actual = exercise.main()
        self.assertEqual(20100, actual.get("sum"))
        self.assertEqual(200, actual.get("size"))
        self.assertEqual(1, actual.get("amin"))
        self.assertEqual(200, actual.get("amax"))
