[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

>> **Python code**

```python

""" 
Make a scatter plot of birth weight vs. mother's age.
Plot percentiles of birth weight vs. mother's age.
Compute Pearson's and Spearman's correlations.
How would you characterize the relationship between these variables
"""
import nsfg
import math
import thinkstats2
import thinkplot
import numpy as np
import pandas

def make_scatter(df):
	thinkplot.Scatter(df.agepreg, df.totalwgt_lb)
	thinkplot.Save(root='stat_7_1_scatter',
				   formats=['png'],
				   xlabel='Mother\'s age', ylabel='Baby\'s birth weight (lb)')

def plot_percentile(df):
	bins = np.arange(10,46,2)
	indices = np.digitize(df.agepreg, bins)
	groups = df.groupby(indices)

	ages = [group.agepreg.mean() for i, group in groups]
	cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]

	thinkplot.PrePlot(3)
	for percent in [75, 50, 25]:
		weights = [cdf.Percentile(percent) for cdf in cdfs]
		label = '%dth' % percent
		thinkplot.Plot(ages, weights, label=label)
	thinkplot.Save(root='stat_7_1_pctl', 
				   formats=['png'],
				   xlabel='Mother\'s age', ylabel='Baby\'s birth weight (lb)')

def P_corr(df):
	# Pearson's Correlation
	xs = np.asarray(df.agepreg)
	ys = np.asarray(df.totalwgt_lb)

	meanx = xs.mean()
	varx = xs.var()
	meany = ys.mean()
	vary = ys.var()

	corr = thinkstats2.Cov(xs,ys,meanx,meany) / math.sqrt(varx * vary)

	return corr

def S_corr(df):
	# Spearman's Correlation
	xranks = pandas.Series(df.agepreg).rank()
	yranks = pandas.Series(df.totalwgt_lb).rank()

	return thinkstats2.Corr(xranks,yranks)

def main():
	df = nsfg.ReadFemPreg()
	live = df[df.outcome == 1]
	df = live.dropna(subset=['agepreg','totalwgt_lb'])

	make_scatter(df) 
	plot_percentile(df)
	print 'Pearson\'s Correlation', P_corr(df)
	print 'Spearman\'s Rank Correlation', S_corr(df)

if __name__ == "__main__":
	main()
```
>> Scatter plot of birth weight versus mother's age:
<img src="/statistics/stat_7_1_scatter.png">

>> Percentiles of birth weight for a range of mother's age bins:
<img src="/statistics/stat_7_1_pctl.png">

>> Pearson's Correlation: 0.0688

>> Spearman's Rank Correlation: 0.0946

>> Seeing from the scatter plot, there's not really a clear relationship between the baby's weight and mother's age.
There is a low positive correlation that indicates that older mothers tend to have heavier babies.
But in general, the plot indicates that regardless of mother's age, baby's weight is relatively constant but slightly linear.	
