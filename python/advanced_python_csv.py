# Part II: Write to CSV File
# create emails.csv file that contains email addresses from Part I

import advanced_python_regex
import csv

df = advanced_python_regex.read_data()
data = advanced_python_regex.email_address(df)

c = csv.writer(open('emails.csv','w'))
for item in data:
  c.writerow([item])
