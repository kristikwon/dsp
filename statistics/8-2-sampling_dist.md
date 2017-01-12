[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

>> **Python code**

```python

""" 
Simulate experiment (n=10, exponential distribution, lamda=2, m=1000), plot sampling distribution of the estimate L.
Compute standard error of the estimate and 90% CI.
Repeat with few different n's and make plot of standard error versus n
"""

"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import math
import thinkstats2
import thinkplot
import numpy as np
import matplotlib.pyplot as pyplot

def Estimate(n,m,lam):
	# simulate experiment
	means = []

	for _ in range(m):
		xs = np.random.exponential(1.0/lam,n)
		L = 1 / np.mean(xs)
		means.append(L)

	# plot sampling distribution
	cdf = thinkstats2.MakeCdfFromList(means)
	CI = cdf.Percentile(5), cdf.Percentile(95)
	stderr = RMSE(means,lam)

	thinkplot.Cdf(cdf)
	pyplot.plot([CI[0],CI[0]],[0,1], color = '0.8')
	pyplot.plot([CI[1],CI[1]],[0,1], color = '0.8')
	pyplot.show()
	thinkplot.Save(root = 'stat_8_2_n%d' %(n),
				   formats = ['png'],
				   xlabel='sample mean', ylabel='CDF')

	print 'Standard Error:', stderr
	print '90% CI: ({0},{1})'.format(CI[0],CI[1])

def RMSE(estimates, actual):
	e2 = [(estimate - actual) ** 2 for estimate in estimates]
	mse = np.mean(e2)
	return math.sqrt(mse)

def main():
	Estimate(10,1000,2)


if __name__ == "__main__":
	main()
```

>> Standard Error: 0.852; 90% CI: (1.311, 3.686) <img src="/statistics/stat_8_2_n10.png">
