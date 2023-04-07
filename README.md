# Advanced Python for Data Science: Intro



[![run unittests](https://github.com/advanced-python-ds/code-as-data/actions/workflows/run_unittests.yml/badge.svg)](https://github.com/advanced-python-ds/code-as-data/actions/workflows/run_unittests.yml)


## This is Advanced Python for Data Science
### Intro Course: Code as Data

In this repo, you can find the coding exercises for the course.
You may use this template repo to work on your code locally.

Link to the course: [Advanced Python for Data Science](https://www.udemy.com/course/4976196)
### Exercise

Welcome to the final exercise of the course!

In the following exercise, you will implement three statistical evaluations on fresh data while treating some of your
code as data.

We recommend you to watch the instructions video before you address this problem. You may find it more comfortable to
work with your own IDE rather than an online editor. You can clone the repo from
here:  [https://github.com/advanced-python-ds/ex-code-as-data]()

#### Background

The TikTok account [@pazpazthecoder](https://www.tiktok.com/@pazpazthecoder?lang=en) for coding and math gets thousands of views per week. The creator is specifically
interested in three reports to track the amount of followers, amount of likes, and average sentiments, per day and per
county.

More specifically, we want to evaluate each of the reports and understand if after aggregation and outliers filtering,
the production model used to predict future activity is still a good representation of the new observations streaming
into the systems.

#### MyEval

You should complete the following program, so it can perform statistical tests on the three csv files, according to the
following specifications:

1. For the likes.csv, data should be aggregated by county and filtered from any counties with less than 2K views total
2. For the followers.csv, data should also be aggregated by county, then filtered from any outliers that distant from
   the mean more than 3 standard deviations
3. For the sentiments.csv , data should be aggregated by a daily weighted average (weight = views), then like
   followers.csv, filtered from any outliers that distant from the mean more than 3 standard deviations.

#### Working with Error Messages

This coding exercise consists of 8 steps total, and understanding error messages towards a successful submission may be
tricky.

For more informative error messages, walk through the '# Step i: ... '  comments sequentially through the exercise.

A failing step message may look like this:

```
######### DETAILS: #########
Step 1.1 Failed. MyEval self.grouper_func attribute isn't set well.
```

When the step is executed successfully, the error message will change to the next following error, until all errors are
resolved.

Good luck!

### Getting the Data
Officially, we1 only support Mac and Linux operating systems. If you are on a Windows machine, we recommend you use [GitHub Codespaces](https://github.com/features/codespaces) as your coding environment.
1. [Set up AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html), if you do not already have one.
2. [Configure AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
3. Install `make`
   1. Mac
      1. [Install Homebrew](https://docs.brew.sh/Installation).
      2. Run: ```brew install make```

   2. Linux:
      1. Run: (you might need to use `sudo`)
      ```
      apt update
      apt install make
      ```
   3. Confirm `make` is installed by running: ```make --version```
4. Run: `make data`
5. Now, you should have three data files in `exercise1/`:
   1. `followers.csv`
   2. `likes.csv`
   3. `sentiments.csv`
