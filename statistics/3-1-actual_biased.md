[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> **Python code:**

```python

"""
Construct actual distribution for the number of children under 18 in the household (numkdhh)
Compute the biased distribution we would see if we surveyed the children and asked them 
how many children under 18 are in their household.
Plot the actual and biased distributions, and compute their means
"""

"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import thinkstats2
import thinkplot
import chap01soln
resp = chap01soln.ReadFemResp()

# Make a PMF of numkdhh, the number of children under 18 in the respondent's household
pmf = thinkstats2.Pmf(resp['numkdhh'])

# Actual PMF
thinkplot.Pmf(pmf,label='actual')

# Define BiasPmf
def BiasPmf(pmf, label):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

# Make biased Pmf of children in the household, as observed if you surveyed the children instead of the respondents
biased_pmf = BiasPmf(pmf,label='observed')

# Display the actual Pmf and the biased Pmf on the same axes
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel='number of children', ylabel='PMF')

# Compute the means of two Pmfs
print 'actual mean', pmf.Mean()
print 'biased mean', biased_pmf.Mean()




```

>> Actual mean: 1.02 children; Biased mean: 2.40 children
<img src="/statistics/stat_3_1_fig1.png">
