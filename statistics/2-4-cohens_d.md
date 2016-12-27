[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> 
**Python Code:

```python

"""
Using the variable totalwgt_lb, investigate whether first babies are 
lighter or heavier than others. COmpute Cohen's d to quantify the 
difference between the groups. How does it compare to the difference 
in pregnancy length?
"""
"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import nsfg
import math

df = nsfg.ReadFemPreg()

# Identify live first and other births
live = df[df.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

# Compute means
mean1 = firsts.totalwgt_lb.mean()
mean2 = others.totalwgt_lb.mean()

# Compute variances
var1 = firsts.totalwgt_lb.var()
var2 = others.totalwgt_lb.var()

# Compute n
n1, n2 = len(firsts.totalwgt_lb), len(others.totalwgt_lb)

# Cohen's d
mean_diff = mean1 - mean2
pooled_var = (n1*var1 + n2*var2) / (n1 + n2)
d = mean_diff / math.sqrt(pooled_var)

# Output results
print 'Mean'
print 'First:', mean1
print 'Others:', mean2

print 'Variance'
print 'First:', var1
print 'Others:', var2

print 'Mean difference:', mean_diff
print 'Cohen\'s d:', d
```
>> Difference of mean weight between first babies and other babies is -0.125 pounds. Cohen's _d_ indiciates that the difference between the two groups is -0.0887 standard deviations, which shows that first babies are slightly lighter than others. This difference is 3 times larger than the difference in mean pregnancy length, which is 0.029 standard deviations. 
