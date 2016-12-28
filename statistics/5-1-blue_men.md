[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> **Python code**

```python

""" 
What percentage of US male population is in the following range: 5'10"-6'1"
"""

import scipy.stats


# Convert given range from inch to cm
def inch_to_cm(height):
	return height * 2.54

# Calculate percent of population with at least given height
def pct_in_range(min_ht, max_ht, mu, sigma):
	diff = (scipy.stats.norm.cdf(max_ht, loc=mu, scale=sigma) - scipy.stats.norm.cdf(min_ht, loc=mu, scale=sigma)) * 100
	print diff

def main():
	mu = 178
	sigma = 7.7

	# Convert inch range to cm
	min_ht = inch_to_cm(70)
	max_ht = inch_to_cm(73)

	pct_in_range(min_ht, max_ht, mu, sigma)

if __name__ == "__main__":
	main()
  
```

>> Since the distribution of heights is normal, given parameters, mu and sigma, are used to model the distribution for men's height. Range of heights, 5'10" and 6'1", are first converted to centimeters to be consistent with the given parameters. scipy.stats.norm.cdf evaluates the percent of male population with at least given height. So share of population in given range is the difference of two CDFs. 34.27% of US male population is in the range of 5'10" and 6'1".
