import sys
from contextlib import contextmanager
from io import StringIO
from unittest import TestCase
import pandas as pd

import exercise

TestCase.maxDiff = None


@contextmanager
def capture_print():
    _stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        yield sys.stdout
    finally:
        sys.stdout = _stdout


def dummy_grouper(i: iter, *args, **kwargs):
    pass


def dummy_filter(i: iter, *args, **kwargs):
    pass


def return_arg_grouper(i: iter, *args, **kwargs):
    return i


def return_first_filter(i: iter, *args, **kwargs):
    return i[:1]


class Evaluate(TestCase):
    def test_evaluate_initialization(self):
        my_eval = exercise.MyEval(grouper_func=dummy_grouper, filter_func=dummy_filter)

        # step 1.1: init (grouper func)
        with self.subTest(case="init grouper function"):
            self.assertEqual(
                dummy_grouper,
                my_eval.grouper_func,
                msg="\n######### DETAILS: ######### \nStep 1.1 Failed. \nMyEval self.grouper_func attribute isn't set "
                    "well",
            )

        with self.subTest(case="init filter function"):
            self.assertEqual(
                dummy_filter,
                my_eval.filter_func,
                msg="\n######### DETAILS: ######### \nStep 1.2 Failed. \nMyEval self.filter_func attribute isn't set "
                    "well",
            )

    def test_evaluate_call(self):
        my_eval = exercise.MyEval(
            grouper_func=return_arg_grouper, filter_func=return_first_filter
        )
        actual = my_eval([1, 2, 3])
        self.assertEqual(
            [1],
            actual,
            msg="\n######### DETAILS: ######### \nStep 2 Failed. \nMyEval __call__ method isn't implemented well",
        )

    def test_views_by_county(self):
        df = pd.DataFrame(data={"county": [1, 1, 2], "likes": [3, 1, 1]})
        expected = [4, 1]
        actual = exercise.get_views_by_county(df)

        with self.subTest(case="return value is a series"):
            self.assertTrue(
                isinstance(actual, pd.Series),
                msg="\n######### DETAILS: ######### \nStep 3 Failed. \nget_views_by_county function isn't implemented "
                    "well - Return value should be a pandas Series.",
            )

        with self.subTest(case="return value regression"):
            self.assertEqual(
                expected,
                list(actual),
                msg="\n######### DETAILS: ######### \nStep 3 Failed. \nget_views_by_county function isn't implemented "
                    "well",
            )

    def test_sentiment_by_day(self):
        df = pd.DataFrame(
            data={
                "date": ["2022-12-01", "2022-12-01", "2022-12-02"],
                "sentiment": [0.6, 1, 0.8],
                "views": [10, 30, 10],
            }
        )
        df["date"] = pd.to_datetime(df["date"])
        expected = [0.9, 0.8]
        actual = exercise.get_sentiment_by_day(df)

        with self.subTest(case="return value is a series"):
            self.assertTrue(
                isinstance(actual, pd.Series),
                msg="\n######### DETAILS: ######### \nStep 4 Failed. \nget_sentiment_by_day function isn't implemented "
                    "well - Return value should be a pandas Series.",
            )
        with self.subTest(case="return value regression"):
            self.assertListEqual(
                expected,
                list(actual),
                msg="\n######### DETAILS: ######### \nStep 4 Failed. \nget_sentiment_by_day function isn't implemented well",
            )

    def test_filter_threshold(self):
        s = pd.Series(data=[200, 300, 400])
        expected = [300, 400]
        actual = exercise.filter_threshold(s)

        with self.subTest(case="return value is a series"):
            self.assertTrue(
                isinstance(actual, pd.Series),
                msg="\n######### DETAILS: ######### \nStep 5 Failed. \nfilter_threshold function isn't implemented well - "
                    "Return value should be a pandas Series.",
            )

        with self.subTest(case="return value regression"):
            self.assertListEqual(
                expected,
                list(actual),
                msg="\n######### DETAILS: ######### \nStep 5 Failed. \nfilter_threshold function isn't implemented well "
                    "when using the default threshold",
            )

    def test_filter_threshold_custom_threshold(self):
        s = pd.Series(data=[1, 2, 3, 4, 5])
        expected = [4, 5]
        actual = exercise.filter_threshold(s, 3)

        self.assertListEqual(
            expected,
            list(actual),
            msg="\n######### DETAILS: ######### \nStep 5 Failed. \nfilter_threshold function isn't implemented well "
                "when using a custom threshold",
        )

    def test_filter_outliers_with_default_threshold(self):
        s = pd.Series(data=[1, 2, 3] * 10 + [-50, 50])
        expected = [1, 2, 3] * 10
        actual = exercise.filter_outliers(s)

        with self.subTest(case="return value is a series"):
            self.assertTrue(
                isinstance(actual, pd.Series),
                msg="\n######### DETAILS: ######### \nStep 6 Failed. \nfilter_outliers function isn't implemented well - "
                    "Return value should be a pandas Series.",
            )

        with self.subTest(case="return value regression"):
            self.assertListEqual(
                expected,
                list(actual),
                msg="\n######### DETAILS: ######### \nStep 6 Failed. \nfilter_outliers function isn't implemented well "
                    "when using the default threshold",
            )

    def test_filter_outliers_with_custom_threshold(self):
        s = pd.Series(data=[1, 2, 3] * 10 + [-50, 50])
        expected = [1, 2, 3] * 10 + [50]
        actual = exercise.filter_outliers(s, 4)

        with self.subTest(case="return value regression"):
            self.assertListEqual(
                expected,
                list(actual),
                msg="\n######### DETAILS: ######### \nStep 6 Failed. \nfilter_outliers function isn't implemented well "
                    "when using a custom threshold",
            )

    def test_tuple_assignment(self):
        with self.subTest(case="likes configuration"):
            self.assertSequenceEqual(
                exercise.TESTS.get("LIKES"),
                ("likes.csv", exercise.get_views_by_county, exercise.filter_threshold),
                msg="\n######### DETAILS: ######### \nStep 7 Failed. \nTuple for likes.csv isn't implemented well",
            )

        with self.subTest(case="followers configuration"):
            self.assertSequenceEqual(
                exercise.TESTS.get("FOLLOWERS"),
                ("followers.csv", exercise.get_views_by_county, exercise.filter_outliers),
                msg="\n######### DETAILS: ######### \nStep 7 Failed. \nTuple for followers.csv isn't implemented well",
            )

        with self.subTest(case="sentiment configuration"):
            self.assertSequenceEqual(
                exercise.TESTS.get("SENTIMENTS"),
                ("sentiments.csv", exercise.get_sentiment_by_day, exercise.filter_outliers),
                msg="\n######### DETAILS: ######### \nStep 7 Failed. \nTuple for sentiments.csv isn't implemented well",
            )
