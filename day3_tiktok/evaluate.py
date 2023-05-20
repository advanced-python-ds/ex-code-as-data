from unittest import TestCase, mock
from unittest.mock import MagicMock

import pandas as pd
from pandas import DatetimeIndex

import exercise


def dummy_grouper(i: iter, *args, **kwargs):
    pass


def dummy_filter(i: iter, *args, **kwargs):
    pass


def return_arg_grouper(i: iter, *args, **kwargs):
    return i


def return_first_filter(i: iter, *args, **kwargs):
    return i[:1]


class TestTiktokReports(TestCase):
    def test_get_values_by_county_return_value(self):
        """
        Test that get_values_by_county returns a pandas Series
        """
        df = pd.DataFrame(data={"county": [1, 1, 2], "views": [3, 1, 1]})
        actual_return = exercise.get_values_by_county(df)
        self.assertIsInstance(
            actual_return,
            pd.Series,
            msg="Return value for get_values_by_county should be a pandas Series.",
        )

    def test_get_values_by_county_with_default_col(self):
        """
        Test that get_values_by_county returns the correct values when col is not specified
        """
        expected_groups = pd.Series(data=[4, 1], index=[1, 2])
        df = pd.DataFrame(data={"county": [1, 1, 2], "views": [3, 1, 1]})
        actual_groups = exercise.get_values_by_county(df)

        pd.testing.assert_series_equal(
            expected_groups, actual_groups, check_names=False
        )

    def test_get_values_by_county_with_col(self):
        """
        Test that get_values_by_county returns the correct values when col is specified
        """
        expected_groups = pd.Series(data=[3, 2], index=[1, 2])
        df = pd.DataFrame(data={"county": [1, 1, 2], "likes": [3, 0, 2]})
        actual_groups = exercise.get_values_by_county(df, col="likes")

        pd.testing.assert_series_equal(
            expected_groups, actual_groups, check_names=False
        )

    def test_get_values_by_county_with_col_that_does_not_exist(self):
        """
        Test that get_values_by_county raises a KeyError when col does not exist
        """
        df = pd.DataFrame(data={"county": [1, 1, 2], "views": [3, 1, 1]})
        with self.assertRaises(KeyError):
            exercise.get_values_by_county(df, col="likes")

    def test_get_sentiment_by_date_return_value(self):
        """
        Test that get_sentiment_by_date returns a pandas Series
        """
        df = pd.DataFrame(
            data={
                "date": ["2022-12-01", "2022-12-01", "2022-12-02"],
                "views": [3, 1, 1],
                "sentiment": [0.5, 1, 0],
            }
        )
        df["date"] = pd.to_datetime(df["date"])
        actual_return = exercise.get_sentiment_by_date(df)
        self.assertIsInstance(
            actual_return,
            pd.Series,
            msg="Return value for get_sentiment_by_day should be a pandas Series.",
        )

    def test_get_sentiment_by_date(self):
        """
        Test that get_sentiment_by_date returns the correct values
        """
        expected_groups = pd.Series(
            data=[0.625, 0],
            index=DatetimeIndex(["2022-12-01", "2022-12-02"], freq="1D"),
        )
        df = pd.DataFrame(
            data={
                "date": ["2022-12-01", "2022-12-01", "2022-12-02"],
                "views": [3, 1, 1],
                "sentiment": [0.5, 1, 0],
            }
        )
        df["date"] = pd.to_datetime(df["date"])
        actual_groups = exercise.get_sentiment_by_date(df)

        pd.testing.assert_series_equal(
            expected_groups, actual_groups, check_names=False
        )

    def test_filter_threshold_return_value(self):
        """
        Test that filter_threshold returns a pandas Series
        """
        series = pd.Series(data=[3, 1, 1])
        actual_return = exercise.filter_threshold(series)
        self.assertIsInstance(
            actual_return,
            pd.Series,
            msg="Return value for filter_threshold should be a pandas Series.",
        )

    def test_filter_threshold_with_default_threshold(self):
        """
        Test that filter_threshold returns the correct values when threshold is not specified
        """
        series = pd.Series(data=[201, 200, -250])
        expected_return = pd.Series(data=[201])
        actual_return = exercise.filter_threshold(series)

        pd.testing.assert_series_equal(
            expected_return, actual_return, check_names=False
        )

    def test_filter_threshold_with_threshold(self):
        """
        Test that filter_threshold returns the correct values when threshold is specified
        """
        series = pd.Series(data=[201, 199, 198])
        expected_return = pd.Series(data=[201, 199])
        actual_return = exercise.filter_threshold(series, threshold=198)

        pd.testing.assert_series_equal(
            expected_return, actual_return, check_names=False
        )

    def test_filter_outliers_return_value(self):
        """
        Test that filter_outliers returns a pandas Series
        """
        series = pd.Series(data=[3, 1, 1])
        actual_return = exercise.filter_outliers(series)
        self.assertIsInstance(
            actual_return,
            pd.Series,
            msg="Return value for filter_outliers should be a pandas Series.",
        )

    def test_filter_outliers_with_default_threshold(self):
        """
        Test that filter_outliers returns the correct values when threshold is not specified
        """
        series = pd.Series(data=[1, 2, 3] * 10 + [-50, 50])
        expected_return = pd.Series(data=[1, 2, 3] * 10)
        actual_return = exercise.filter_outliers(series)

        pd.testing.assert_series_equal(
            expected_return, actual_return, check_names=False
        )

    def test_filter_outliers_with_threshold(self):
        """
        Test that filter_outliers returns the correct values when threshold is specified
        """
        series = pd.Series(data=[1, 2, 3] * 10 + [-50, 50])
        expected_return = pd.Series(
            data=[1, 2, 3] * 10 + [50], index=list(range(30)) + [31]
        )
        actual_return = exercise.filter_outliers(series, threshold=4)

        pd.testing.assert_series_equal(expected_return, actual_return)

    def test_my_eval_instantiation_without_kwargs(self):
        """
        Test that MyEval can be instantiated with grouper function and filter function
        """
        my_eval = exercise.MyEval(dummy_grouper, dummy_filter)
        self.assertEqual(
            my_eval.grouper_func,
            dummy_grouper,
            msg="grouper_func isn't initialized correctly",
        )
        self.assertEqual(
            my_eval.filter_func,
            dummy_filter,
            msg="filter_func isn't initialized correctly",
        )

    def test_my_eval_instantiation_with_kwargs(self):
        """
        Test that MyEval can be instantiated with grouper function, filter function and kwargs
        """
        my_eval = exercise.MyEval(
            dummy_grouper, dummy_filter, {"col": "views"}, {"threshold": 2}
        )
        self.assertEqual(
            my_eval.grouper_func,
            dummy_grouper,
            msg="grouper_func isn't initialized correctly",
        )
        self.assertEqual(
            my_eval.filter_func,
            dummy_filter,
            msg="filter_func isn't initialized correctly",
        )
        self.assertEqual(
            my_eval.grouper_kwargs,
            {"col": "views"},
            msg="grouper kwargs aren't initialized correctly",
        )
        self.assertEqual(
            my_eval.filter_kwargs,
            {"threshold": 2},
            msg="filter kwargs aren't initialized correctly",
        )

    def test_my_eval_instantiation_without_filter_func(self):
        with self.assertRaises(
            TypeError,
            msg="MyEval should raise TypeError if filter_func is not specified",
        ):
            exercise.MyEval(dummy_grouper)
        with self.assertRaises(
            TypeError,
            msg="MyEval should raise TypeError if grouper_func is not specified",
        ):
            exercise.MyEval(filter_func=dummy_grouper)

    def test_my_eval_call(self):
        """
        Test the correct sequence of function calls when MyEval is called
        """
        expected = pd.Series(data=[1])
        data = pd.Series([1, 2, 3, 4, 5, 6])
        my_eval = exercise.MyEval(
            grouper_func=return_arg_grouper, filter_func=return_first_filter
        )
        actual = my_eval(data)

        pd.testing.assert_series_equal(expected, actual, check_names=False)

    def test_my_eval_calls(self):
        """
        Test the correct sequence of function calls when MyEval is instantiated without kwargs
        """
        mock_return_grouper = MagicMock()
        mock_grouper = MagicMock(return_value=mock_return_grouper)
        mock_filter = MagicMock()
        mock_df = MagicMock()
        my_eval = exercise.MyEval(mock_grouper, mock_filter)
        my_eval(mock_df)

        mock_grouper.assert_called_with(mock_df)
        mock_filter.assert_called_with(mock_return_grouper)

    def test_my_eval_calls_with_kwargs(self):
        """
        Test the correct sequence of function calls when MyEval is instantiated with kwargs
        """
        mock_return_grouper = MagicMock()
        mock_grouper = MagicMock(return_value=mock_return_grouper)
        mock_filter = MagicMock()
        mock_df = MagicMock()
        my_eval = exercise.MyEval(
            mock_grouper, mock_filter, {"col": "views"}, {"threshold": 2}
        )
        my_eval(mock_df)

        mock_grouper.assert_called_with(mock_df, col="views")
        mock_filter.assert_called_with(mock_return_grouper, threshold=2)

    @mock.patch("exercise.pd.read_csv")
    def test_main_my_eval_keys(self, mock_read_csv):
        """
        Test that main returns a dictionary with 3 keys, one for each report
        """
        df = pd.DataFrame(
            data={
                "date": ["2019-01-01", "2019-01-01", "2019-01-01", "2019-01-01"],
                "county": ["A", "A", "B", "B"],
                "views": [1, 2, 3, 4],
                "sentiment": [0.1, 0.2, 0.3, 0.4],
                "likes": [10, 20, 30, 40],
                "followers": [100, 200, 300, 400],
            }
        )
        df["date"] = pd.to_datetime(df["date"])
        mock_read_csv.return_value = df

        actual = exercise.main()

        self.assertEqual(
            3,
            len(actual),
            msg="main should return a dictionary with 3 keys, one for each report",
        )
        self.assertListEqual(
            ["likes.csv", "followers.csv", "sentiments.csv"],
            list(actual.keys()),
            msg="main should return a dictionary with 3 keys, one for each report",
        )

    @mock.patch("exercise.pd.read_csv")
    def test_main_return_values(self, mock_read_csv):
        """
        Test that main returns the correct values
        :param mock_read_csv:
        :return:
        """
        df = pd.DataFrame(
            data={
                "date": [
                    "2019-01-01",
                    "2019-01-02",
                    "2019-01-03",
                    "2019-01-01",
                    "2019-01-02",
                    "2019-01-03",
                    "2019-01-01",
                    "2019-01-02",
                    "2019-01-03",
                    "2019-01-01",
                    "2019-01-02",
                    "2019-01-03",
                ],
                "county": ["A", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"],
                "views": [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],
                "sentiment": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                "likes": [100, 200, 30, 40, 10, 20, 30, 40, 50, 60, 70, 80],
                "followers": [1, 5, 3, 4, 5, -1000, 7, 8, 9, 10, 11, 12],
            }
        )
        df["date"] = pd.to_datetime(df["date"])
        mock_read_csv.return_value = df

        actual = exercise.main()
        expected_likes = pd.Series([300], index=["A"])
        expected_followers = pd.Series(
            [6, 3, 4, 5, 7, 8, 9, 10, 11, 12],
            index=["A", "B", "C", "D", "F", "G", "H", "I", "J", "K"],
        )
        expected_sentiments = pd.Series(
            [0.4, 0.6, 0.4],
            index=DatetimeIndex(["2019-01-01", "2019-01-02", "2019-01-03"], freq="1D"),
        )

        pd.testing.assert_series_equal(
            expected_likes, actual["likes.csv"], check_names=False
        )
        pd.testing.assert_series_equal(
            expected_followers,
            actual["followers.csv"],
            check_names=False,
        )
        pd.testing.assert_series_equal(
            expected_sentiments, actual["sentiments.csv"], check_names=False
        )
