# Part III: Dictionary

import pandas as pd

def read_data():
	faculty = pd.read_csv('faculty.csv')
	return faculty


'''
Q6: create dictionary in following format:
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
Print the first 3 key and value pairs of the dictionary              
'''
def dict_format1(df):
	# df = DataFrame
	# create a dictionary of degrees
	faculty_dict = dict()

	# need to do some data cleaning first:
	# Separate first, middle, and last name. If first name is single letter, define middle as the first name
	for i in range(0,len(df)):
		name_clean = df['name'][i].replace('.','').replace('(','').replace(')','').split()
		degree_clean = df[' degree'][i].strip()
		title_clean = df[' title'][i].replace(' of Biostatistics','').replace(' is Biostatistics','')

		if len(name_clean) == 2:
			first_name = name_clean[0]
			last_name = name_clean[1]
		else:
			if len(name_clean[0]) == 1:
				first_name = name_clean[1]
				middle_name = name_clean[0]
				last_name = name_clean[2]
			else:
				first_name = name_clean[0]
				middle_name = name_clean[1]
				last_name = name_clean[2]

		# Populate dictionary
		if last_name in faculty_dict:
			faculty_dict[last_name].append([degree_clean,title_clean,df[' email'][i]])
		else:
			faculty_dict[last_name] = [[degree_clean,title_clean,df[' email'][i]]]
	return faculty_dict


'''
Q7: create dictionary in following format:
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }

Print the first 3 key and value pairs of the dictionary              
'''
def dict_format2(df):
	# create a dictionary of degrees
	professor_dict = dict()

	# need to do some data cleaning first:
	# Separate first, middle, and last name. If first name is single letter, define middle as the first name
	for i in range(0,len(df)):
		name_clean = df['name'][i].replace('.','').replace('(','').replace(')','').split()
		degree_clean = df[' degree'][i].strip()
		title_clean = df[' title'][i].replace(' of Biostatistics','').replace(' is Biostatistics','')

		if len(name_clean) == 2:
			first_name = name_clean[0]
			last_name = name_clean[1]
		else:
			if len(name_clean[0]) == 1:
				first_name = name_clean[1]
				middle_name = name_clean[0]
				last_name = name_clean[2]
			else:
				first_name = name_clean[0]
				middle_name = name_clean[1]
				last_name = name_clean[2]

		# Populate dictionary
		if (first_name,last_name) in professor_dict:
			professor_dict[(first_name,last_name)].append([degree_clean,title_clean,df[' email'][i]])
		else:
			professor_dict[(first_name,last_name)] = [[degree_clean,title_clean,df[' email'][i]]]
	return professor_dict


'''
Q8: Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors
'''
def dict_format3(df):
	# create a dictionary of degrees
	professor_dict = dict()

	# need to do some data cleaning first:
	# Separate first, middle, and last name. If first name is single letter, define middle as the first name
	for i in range(0,len(df)):
		name_clean = df['name'][i].replace('.','').replace('(','').replace(')','').split()
		degree_clean = df[' degree'][i].strip()
		title_clean = df[' title'][i].replace(' of Biostatistics','').replace(' is Biostatistics','')

		if len(name_clean) == 2:
			first_name = name_clean[0]
			last_name = name_clean[1]
		else:
			if len(name_clean[0]) == 1:
				first_name = name_clean[1]
				middle_name = name_clean[0]
				last_name = name_clean[2]
			else:
				first_name = name_clean[0]
				middle_name = name_clean[1]
				last_name = name_clean[2]

		# Populate dictionary
		if (last_name,first_name) in professor_dict:
			professor_dict[(last_name,first_name)].append([degree_clean,title_clean,df[' email'][i]])
		else:
			professor_dict[(last_name,first_name)] = [[degree_clean,title_clean,df[' email'][i]]]
	return professor_dict


def dict_format_out(faculty_dict,n):
	# Once dictionary is complete, sort key by key and print out the first 3 items
	for key in sorted(faculty_dict)[:n]:
		print "%s: %s" % (key, faculty_dict[key])




#Q6
dict_format_out(dict_format1(read_data()),3)
#Q7
dict_format_out(dict_format2(read_data()),3)
#Q8
dict_format_out(dict_format3(read_data()),len(read_data()))
