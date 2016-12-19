'''
1. find how many diff degrees there are, and their frequencies (phd, scd, md, mph, etc)
2. find how many diff titles there are and their frequencies (assitant professor, professor, etc)
3. search for email addresses and put them in a list. print the list of email addresses
4. find how many diff email domains there are. print list of unique email domains
'''

import pandas as pd 

def read_data():
	faculty = pd.read_csv('faculty.csv')
	return faculty


def n_degree(df):
	# df = DataFrame
	# create a dictionary of degrees
	d = dict()

	# need to do some data cleaning first
	for i in range(0,len(df)):
		degree_clean = df[' degree'][i].replace('.','')
		degree_clean = df[' degree'][i].split()
	
		# count the number of degrees
		for j in range(0,len(degree_clean)):
			if degree_clean[j] not in d:
				d[degree_clean[j]] = 1
			else:
				d[degree_clean[j]] += 1
	return d


def n_title(df):
	# df = DataFrame
	# create a dictionary of degrees
	d = dict()

	# data cleaning
	for i in range(0,len(df)):
		title_clean = df[' title'][i].replace(' of Biostatistics','')
		title_clean = title_clean.replace(' is Biostatistics','')
		if title_clean not in d:
			d[title_clean] = 1
		else:
			d[title_clean] += 1
	return d


def email_address(df):
	# df = DataFrame
	email_list = []
	for i in range(0,len(df)):
		email_list.append(df[' email'][i])
	return email_list


def n_email_domain(df):
	# df = DataFrame
	# create a dictionary of email-domains
	d = dict()

	#data cleaning
	for i in range(0,len(df)):
		domain_clean = df[' email'][i].split('@')[1]
		if domain_clean not in d:
			d[domain_clean] = 1
		else:
			d[domain_clean] += 1
	return d


#Q1
print n_degree(read_data())
#Q2
print n_title(read_data())
#Q3
print email_address(read_data())
#Q4
print n_email_domain(read_data())
