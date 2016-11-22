# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'

from datetime import date

def date_form_a(d):
    return date(int(d[6:]),int(d[:2]),int(d[3:5]))

def delta_days(start,stop): # start and stop are in date format
    return (stop - start).days
  
print delta_days(date_form_a(date_start),date_form_a(date_stop))



####b)  
date_start = '12312013'  
date_stop = '05282015'  

def date_form_b(d):
    return date(int(d[4:]),int(d[:2]),int(d[2:4]))
    
print delta_days(date_form_b(date_start),date_form_b(date_stop))


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

#create dictionary of months to integer values
months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

def date_form_c(d):
    return date(int(d[7:]),months[d[3:6]],int(d[:2]))
    
print delta_days(date_form_c(date_start),date_form_c(date_stop))
