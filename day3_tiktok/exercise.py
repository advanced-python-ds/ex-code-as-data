from typing import Callable, Optional, Any

import numpy as np
import pandas as pd
from scipy import stats


# Step 1: Implement MyEval __init__ method
class MyEval:
    def __init__(
        self,
        grouper_func: Callable[[pd.DataFrame], pd.Series],
        filter_func: Callable[[pd.Series, Optional[Any]], pd.Series],
    ):
        """
        :param grouper_func: how to group the data
        :param filter_func: how to filter the data
        """
        self.grouper_func = grouper_func
        self.filter_func = filter_func

    # Step 2: Implement MyEval __call__ method, so it first groups the df argument and then filters it
    def __call__(self, df: pd.DataFrame) -> pd.Series:
        """
        :return: grouped and filtered data by the instance callables
        """
        groups = self.grouper_func(df)
        filtered = self.filter_func(groups)
        return filtered

    # The __repr__ method is already implemented for you!
    def __repr__(self):
        """
        :return: A string representation of the class instance
        """
        return (
            f"MyEval instance by "
            f"\ngrouper_func: {self.grouper_func}, "
            f"\nfilter_func: {self.filter_func}"
        )


# Step 3: Implement get_views_by_county function. Use groupby to group df by county.
def get_views_by_county(df: pd.DataFrame) -> pd.Series:
    """
    Get the total views per county
    """
    col = [i for i in df.columns if i not in ["date", "county", "views"]][0]
    return df.groupby("county")[col].sum()


# Step 4: Implement get_sentiment_by_day function. df should be grouped by day and return a weighted average of
# sentiments (weights = views).
def get_sentiment_by_day(df: pd.DataFrame) -> pd.Series:
    """
    Group by day the weighted average of sentiments
    """
    return df.groupby(pd.Grouper(key="date", freq="1D")).apply(
        lambda x: np.average(x.sentiment, weights=x.views)
    )


# Step 5: Implement filter_threshold function. Return a series of values that are grater than the threshold.
def filter_threshold(series: pd.Series, threshold: Optional[int] = 200) -> pd.Series:
    """
    Filter a dataframe by a minimal threshold
    """
    return series[series > threshold]


# Step 6: Implement filter_outliers function. Return a series of values that distant from the mean less than 3
# standard deviations
def filter_outliers(series: pd.Series, threshold: Optional[float] = 3.0) -> pd.Series:
    """
    Filter out outliers by an absolute Zscore threshold
    """
    zscore = np.abs(stats.zscore(series))
    return series[zscore < threshold]


# Step 7: Leverage code-as-data concept to execute the three evaluations!
# Each tuple should include three objects:
# the path to the csv file (e.g. "likes.csv")
# a grouper function
# a filter function.
TESTS = {
    # likes.csv should be evaluated using aggregations by county and filter by threshold
    "LIKES": ("likes.csv", get_views_by_county, filter_threshold),
    # followers.csv should be evaluated using aggregations by county and filter outliers
    "FOLLOWERS": ("followers.csv", get_views_by_county, filter_outliers),
    # sentiments.csv should be evaluated using aggregations by daily weighted average and filter outliers
    "SENTIMENTS": ("sentiments.csv", get_sentiment_by_day, filter_outliers),
}


# Step 8: Integration
# If all functions, methods and assignments are completed well, you should pass all tests.
def execute():
    for name, args in TESTS.items():
        print("Running {}".format(name))

        data = pd.read_csv(args[0], parse_dates=["date"])
        my_eval = MyEval(*args[1:])

        print(my_eval(data))


if __name__ == "__main__":
    execute()
