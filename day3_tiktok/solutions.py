from pprint import pprint
from typing import Callable, Optional, Dict

import numpy as np
import pandas as pd
from scipy import stats


def get_values_by_county(df: pd.DataFrame, col="views") -> pd.Series:
    """
    Get the total values per county
    :param df: dataframe to group
    :param col: column to group by
    :return: sum of column per county
    """
    return df.groupby("county")[col].sum()


def get_sentiment_by_date(df: pd.DataFrame, **kwargs) -> pd.Series:
    """
    Group by day the weighted average (weight = views) of sentiments
    :param df: dataframe to group
    :param kwargs: additional arguments to pass to the groupby function
    :return: weighted average of sentiments per day
    """
    return df.groupby(pd.Grouper(key="date", freq="1D")).apply(
        lambda x: np.average(x.sentiment, weights=x.views)
    )


def filter_threshold(series: pd.Series, threshold: Optional[float] = 200) -> pd.Series:
    """
    Filter a series of values by a threshold
    :param series: series to filter
    :param threshold: threshold to filter by
    :return: values of the series that are grater than the threshold
    """
    return series[series > threshold]


def filter_outliers(series: pd.Series, threshold: Optional[float] = 3.0) -> pd.Series:
    """
    Filter a series of values by a distance from the mean
    :param series: series to filter
    :param threshold: standard deviations count to filter by
    :return: values of the series that their distance from the mean is less than the amount of standard deviations
    """
    zscore = np.abs(stats.zscore(series))
    return series[zscore < threshold]


class MyEval:
    def __init__(
        self,
        grouper_func: Callable[[pd.DataFrame, Optional[str]], pd.Series],
        filter_func: Callable[[pd.DataFrame, Optional[float]], pd.Series],
        grouper_kwargs: dict = None,
        filter_kwargs: dict = None,
    ):
        """
        Instantiate a new MyEval instance with the required configurations
        :param grouper_func: how to group the data
        :param filter_func: how to filter the data
        :param grouper_kwargs: additional arguments to pass to the grouper function
        :param filter_kwargs: additional arguments to pass to the filter function
        """
        self.grouper_func = grouper_func
        self.filter_func = filter_func
        self.grouper_kwargs = grouper_kwargs
        self.filter_kwargs = filter_kwargs

    def __call__(self, df: pd.DataFrame) -> pd.Series:
        """
        group and filter the dataframe according to the MyEval instance configurations
        :return: grouped and filtered data by the instance callables
        """
        groups = self.grouper_func(df, **(self.grouper_kwargs or {}))
        filtered = self.filter_func(groups, **(self.filter_kwargs or {}))
        return filtered


def main():
    """
    Run MyEval on each of the .csv files
    The test variable is a dictionary of the required tests.
    Each test is a tuple of the file name and the MyEval instance with specified grouper and filter functions,
    and additional grouper_kwargs when required.

    :return: a dictionary of the results of each test
    """
    tests: Dict[str, MyEval] = {
        # likes.csv should be evaluated using aggregations by county (with col = likes) and filter by threshold
        "likes.csv": MyEval(
            get_values_by_county, filter_threshold, grouper_kwargs={"col": "likes"}
        ),
        # followers.csv should be evaluated using aggregations by county (with col = followers) and filter outliers
        "followers.csv": MyEval(
            get_values_by_county,
            filter_outliers,
            grouper_kwargs={"col": "followers"},
        ),
        # sentiments.csv should be evaluated using aggregations by daily weighted average and filter outliers
        "sentiments.csv": MyEval(get_sentiment_by_date, filter_outliers),
    }

    return {
        path: my_eval(pd.read_csv(path, parse_dates=["date"]))
        for path, my_eval in tests.items()
    }


if __name__ == "__main__":
    # For your reference
    pprint(main())
