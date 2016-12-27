[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> **Python code**

```python

""" 
Generate 1000 numbers from random.random and plot their PMF and CDF
Is the distribution uniform?
"""

"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import random
import thinkstats2
import thinkplot

# Generate 1000 random numbers
random_list = [random.random() for x in range(1000)]


# Plot pmf and cdf
pmf = thinkstats2.Pmf(random_list)
thinkplot.Pmf(pmf, label = 'PMF')
thinkplot.Show()

cdf = thinkstats2.Cdf(random_list)
thinkplot.Cdf(cdf, label = 'CDF')
thinkplot.Show()
```
<img src="statistics/stat_4_2_pmf.png">
<img src="statistics/stat_4_2_cdf.png">
>> From the PMF graph above, it's difficult to tell whether the distribution is uniform. But the straight, diagonal line of CDF graph indicates that the distribution is uniform. Any same increment of values between 0 and 1 are equally likely to be generated.
