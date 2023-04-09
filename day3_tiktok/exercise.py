from typing import Callable, Optional, Any
import pandas as pd
import numpy as np
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
        self.grouper_func = None  # todo: what should be the grouper_func?
        self.filter_func = None  # todo: what should be the filter_func?

    # Step 2: Implement MyEval __call__ method, so it first groups the df argument and then filters it
    def __call__(self, df: pd.DataFrame) -> pd.Series:
        """
        :return: grouped and filtered data by the instance callables
        """
        pass

    # The __repr__ method is already implemented for you!
    def __repr__(self):
        """
        :return: A string representation of the class instance
        """
        return f"MyEval instance by " \
               f"\ngrouper_func: {self.grouper_func}, " \
               f"\nfilter_func: {self.filter_func}"


# Step 3: Implement get_views_by_county function. Use groupby to group df by county.
def get_views_by_county(df: pd.DataFrame) -> pd.Series:
    """
    Get the total views per county
    """
    pass


# Step 4: Implement get_sentiment_by_day function. df should be grouped by day and return a weighted average of
# sentiments (weights = views).
def get_sentiment_by_day(df: pd.DataFrame) -> pd.Series:
    """
    Group by day the weighted average of sentiments
    """
    pass


# Step 5: Implement filter_threshold function. Return a series of values that are grater than the threshold.
def filter_threshold(series: pd.Series, threshold: Optional[int] = 200) -> pd.Series:
    """
    Filter a dataframe by a minimal threshold
    """
    pass


# Step 6: Implement filter_outliers function. Return a series of values that distant from the mean less than 3
# standard deviations
def filter_outliers(series: pd.Series, threshold: Optional[float] = 3.0) -> pd.Series:
    """
    Filter out outliers by an absolute Zscore threshold
    """
    pass


# Step 7: Leverage code-as-data concept to execute the three evaluations!
# Each tuple should include three objects:
# the path to the csv file (e.g. "likes.csv")
# a grouper function
# a filter function.
TESTS = {
    # likes.csv should be evaluated using aggregations by county and filter by threshold
    "LIKES": (),
    # followers.csv should be evaluated using aggregations by county and filter outliers
    "FOLLOWERS": (),
    # sentiments.csv should be evaluated using aggregations by daily weighted average and filter outliers
    "SENTIMENTS": (),
}


# Step 8: Integration
# If all functions, methods and assignments are completed well, you should pass all tests.
def execute():
    for name, args in TESTS.items():
        print("Running {}".format(name))

        data = pd.read_csv(None,  # todo: read the csv path from args
                           parse_dates=['date'])
        my_eval = MyEval(None, None)  # todo: use 2nd and 3rd objects in args to make a MyEval instance

        print(my_eval(data))


if __name__ == "__main__":
    execute()
