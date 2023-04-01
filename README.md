# Advanced Python for Data Science: Intro



[![run unittests](https://github.com/advanced-python-ds/code-as-data/actions/workflows/run_unittests.yml/badge.svg)](https://github.com/advanced-python-ds/code-as-data/actions/workflows/run_unittests.yml)


## This is Advanced Python for Data Science
### Intro Course: Code as Data

In this repo, you can find the coding exercises for the course.
You may use this template repo to work on your code locally.

Link to the course: [Advanced Python for Data Science](https://www.udemy.com/course/4976196)

### Getting the Data
1. [Set up AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html), if you do not already hav one.
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
   2`likes.csv`
   3`sentiments.csv`
