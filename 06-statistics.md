# Learn Statistics

Time to freshen up your statistics knowledge! We have a guide for
doing exactly that. The exercises go hand in hand with these, so
please check both of them.

There are 6 required and 6 optional problems. Do them while you're
reading the relevant statistics chapters.


## Statistics

[![Think Stats](img/think_stats.jpg)](http://greenteapress.com/thinkstats2/)

[![Think Bayes](img/think_bayes.png)](http://greenteapress.com/thinkbayes/)

Allen Downey wrote great short books to introduce statistics in a fun
way, going over examples and exercises using python. They are freely
available to boot.


### Think Stats Chapters 1 - 9

Think Stats is a great book to both refresh/learn the most critical
statistics topics and gain experience in how you'd apply statistics
analysis to problems using python. It covers typical statistics topics
from a modern, simulation/coding based perspective. The chapters are
quite concise and easy to read.

You can download a PDF or read the book online
[here](http://www.greenteapress.com/thinkstats2/). Of course, if you
are so inclined, you can also buy a hard copy on Amazon, but that is
not necessary.

We will be focusing on the **first 9 chapters**. You can go through
these chapters in 6 to 9 hours (depending on how familiar you are with
statistics and python) Please do so. If it takes somewhat longer,
that's fine. However, don't get stuck too long on a single chapter.
This preparation will help you a lot, and it will provide a good
initial exposure to using python for data analysis, but it is not your
only chance to internalize these topics. If at any point you feel
overwhelmed, don't worry. You don't need to master all of this in
prework.

5 of the 6 required exercises are also from this book. It would be a
good idea to tackle these exercises as you work your way through the
book. For example, the first exercise is 2.4 at the end of chapter 2.
The best time to start working on it is after you read Chapter 2.

If you can finish the required exercises with time to spend, we
suggest working on some of the optional ones. These may take longer,
but will definitely improve your skills and bootcamp experience. Take
your time with these exercises, don't rush them. Don't push yourself
to finish any of them, if you're short on time. Even completing a
single of these is an excellent bonus.


### Think Bayes Chapters 1 & 2

Another important subject is the Bayesian approach to probability,
where _probability_ is approached as _the state of knowledge_ rather
than the _expected frequency_ of things. This Bayesian approach is
used in a lot of data science applications. Luckily, Downey used his
method in Think Stats to write another free introduction book on Bayes
with python-based examples and exercises. It is called Think Bayes and
you can find it [here](http://www.greenteapress.com/thinkbayes/).

Please read the first two chapters of this book will work both as a
reinforcement of probabilities (covered by Think Stats as well) and an
introduction to the Bayesian framework.

The last required exercise is from Think Bayes, and two optional
exercises are also Bayesian problems.


## Exercises

These exercises are a great way to both prepare you for the bootcamp
and for you to assess if you've absorbed the prework content and are
fully ready. There are 6 required and 6 optional problems. We chose
them to go along with your prework statistics training. They require
(and teach) both python and statistics skills. Have fun!

**Every exercise must be finished before your first day of Metis.**


### Setup

As mentioned in the *Preface* of Think Stats (section *Using the Code*), there is some accompanying code and data.
You can get these from the [Think Stats repository](https://github.com/AllenDowney/ThinkStats2).
*Using the Code* explains different ways of getting these files if you are unfamiliar with github.
This repository also includes some ipython notebooks.

We will learn, use and get very familiar with ipython notebooks in class,
but if you want to learn more about them ahead of time to use them for these exercises,
you can check out the [documentation](http://ipython.org/ipython-doc/stable/notebook/notebook.html). You can also optionally try your hand at Think Stats Exercise 1.1, which gives you an ipython notebook and asks a few questions.

### Required Exercises

Please complete and submit your answers:

_Think Stats_
[Exercise 2.1](statistics/exercise_2.1.py)
[Exercise 2.4](statistics/exercise_2.4.py)
[Exercise 3.1](statistics/exercise_3.1.py)
[Exercise 4.2](statistics/exercise_4.2.py)

_Think Bayes_
[Exercise 7.1](statistics/exercise_7.1.py)
[Exercise 8.2](statistics/exercise_8.2.py)


### Optional Exercises

#### 1) Think Stats Exercise 5.1

In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters *µ* = 178 cm and *σ* = 7.7 cm for men, and *µ* = 163 cm and *σ* = 7.3 cm for women.

In order to join Blue Man Group, you have to be male between 5'10" and 6'1" (see [their webpage](http://bluemancasting.com)). What percentage of the U.S. male population is in this range? Hint: use `scipy.stats.norm.cdf`.


#### 2) Think Stats Exercise 6.1

The distribution of income is famously skewed to the right. In this exercise, we’ll measure how strong that skew is.

The Current Population Survey (CPS) is a joint effort of the Bureau of Labor Statistics and the Census Bureau to study income and related variables. Data collected in 2013 is available from the Census Burea’s website. I downloaded `hinc06.xls`, which is an Excel spreadsheet with information about household income, and converted it to `hinc06.csv`, a CSV file you will find in the repository for this book. You will also find `hinc2.py`, which reads this file and transforms the data.

The dataset is in the form of a series of income ranges and the number of respondents who fell in each range. The lowest range includes respondents who reported annual household income “Under $5000.” The highest range includes respondents who made “$250,000 or more.”

To estimate mean and other statistics from these data, we have to make some assumptions about the lower and upper bounds, and how the values are distributed in each range. `hinc2.py` provides `InterpolateSample`, which shows one way to model this data. It takes a `DataFrame` with a column, `income`, that contains the upper bound of each range, and `freq`, which contains the number of respondents in each frame.

It also takes `log_upper`, which is an assumed upper bound on the highest range, expressed in log10 dollars. The default value, `log_upper=6.0` represents the assumption that the largest income among the respondents is 106, or one million dollars.

`InterpolateSample` generates a pseudo-sample; that is, a sample of household incomes that yields the same number of respondents in each range as the actual data. It assumes that incomes in each range are equally spaced on a log10 scale.

Compute the median, mean, skewness and Pearson’s skewness of the resulting sample. What fraction of households reports a taxable income below the mean? How do the results depend on the assumed upper bound?

#### 3) Think Stats Exercise 8.3

In games like hockey and soccer, the time between goals is
roughly exponential. So you could estimate a team’s goal-scoring rate by
observing the number of goals they score in a game. This estimation process
is a little different from sampling the time between goals, so let’s see
how it works.

Write a function that takes a goal-scoring rate, `lam`, in goals per game, and
simulates a game by generating the time between goals until the total time
exceeds 1 game, then returns the number of goals scored.
Write another function that simulates many games, stores the estimates of
`lam`, then computes their mean error and RMSE.

Is this way of making an estimate biased? Plot the sampling distribution of
the estimates and the 90% confidence interval. What is the standard error?
What happens to sampling error for increasing values of `lam`?

#### 4) Think Stats Exercise 9.2

In “Testing a Difference in Means” on page 104, we simulated the null hypothesis by permutation; that is, we treated the observed values as if they represented the entire population, and randomly assigned the members of the population to the two groups.

An alternative is to use the sample to estimate the distribution for the population, then draw a random sample from that distribution. This process is called resampling. There are several ways to implement resampling, but one of the simplest is to draw a sample with replacement from the observed values, as in “Power” on page 112.

Write a class named `DiffMeansResample` that inherits from `DiffMeansPermute` and overrides `RunModel` to implement resampling, rather than permutation.

Use this model to test the differences in pregnancy length and birth weight. How much does the model affect the results?


#### 5) The Elvis Twin Problem
Elvis Presley had a twin brother who died at birth.  What is the probability that Elvis was an identical twin?

*To answer this one, you need some background information:
According to the Wikipedia article on twins:  "Twins are estimated to be approximately 1.9% of the world population, with monozygotic twins making up 0.2% of the total---and 8% of all twins."*


#### 6) The Locomotive Problem
A railroad numbers its locomotives in order 1..N. One day you see a locomotive with the number 60. Estimate how many locomotives the railroad has.

*Hint: Think Bayes Chapter 3 actually solves this ambiguous looking problem. It’s a pretty cool problem to solve with a Bayesian approach. Try thinking about it and coming up with an answer before looking at the chapter.*