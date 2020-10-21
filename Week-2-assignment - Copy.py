# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 18:17:30 2015

@author: Omar Elfarouk
"""

import pandas
import numpy
import scipy.stats
import seaborn
import matplotlib.pyplot as plt


data = pandas.read_csv('gapminder.csv', low_memory=False)



# new code setting variables you will be working with to numeric
data['Alcoholuse'] = pandas.to_numeric(data['Alcoholuse'], errors='coerce')
data['Income'] = pandas.to_numeric(data['Income'], errors='coerce')
data['suicideper100th'] = pandas.to_numeric(data['suicideper100th'], errors='coerce')


#subset data the excel sheet available , and data wrangling
sub1=data
sub1 = sub1.replace(r'\s+', 0, regex=True) #Replace empty strings with zero
#sub1=data[(data['AGE']>=18) & (data['AGE']<=25) & (data['CHECK321']==1)]

#make a copy of my new subsetted data
sub2 = sub1.copy()

# recode missing values to python missing (NaN)
#sub2['Alcoholuse']=sub2['Alcoholuse'].replace(0, numpy.nan)
#sub2['Income']=sub2['Income'].replace(0, numpy.nan)
#sub2['suicideper100th']=sub2['suicideper100th'].replace(0, numpy.nan)
#recoding values for S3AQ3B1 into a new variable, USFREQMO
#recode1 = {1: 30, 2: 22, 3: 14, 4: 6, 5: 2.5, 6: 1}
#sub2['USFREQMO']= sub2['S3AQ3B1'].map(recode1)

# contingency table of observed counts
ct1=pandas.crosstab(sub2['Alcoholuse'], sub2['Income'])
print (ct1)

# column percentages
colsum=ct1.sum(axis=0)
colpct=ct1/colsum
print(colpct)

# chi-square
print ('chi-square value, p value, expected counts')
cs1= scipy.stats.chi2_contingency(ct1)
print (cs1)

# set variable types 
sub2["Income"] = sub2["Income"].astype('category')
# new code for setting variables to numeric:
sub2['Alcoholuse'] = pandas.to_numeric(sub2['Alcoholuse'], errors='coerce')

# old code for setting variables to numeric:
#sub2['TAB12MDX'] = sub2['TAB12MDX'].convert_objects(convert_numeric=True)

# graph percent with nicotine dependence within each smoking frequency group 
seaborn.factorplot(x="Income", y="Alcoholuse", data=sub2, kind="bar", ci=None)
plt.xlabel('Income below or greater than 2000USD')
plt.ylabel('Alcohol consumption rate')

recode2 = {0: 0, 1: 1}
sub2['COMP1v1']= sub2['Alcoholuse'].map(recode2)

# contingency table of observed counts
ct2=pandas.crosstab(sub2['Income'], sub2['COMP1v1'])
print (ct2)

# column percentages for creating the column sum
colsum=ct2.sum(axis=0)
colpct=ct2/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs2= scipy.stats.chi2_contingency(ct2)
print (cs2)

recode3 = {1: 1, 2: 2}
sub2['COMP1v2']= sub2['Alcoholuse'].map(recode3)

# contingency table of observed counts
ct3=pandas.crosstab(sub2['Income'], sub2['COMP1v2'])
print (ct3)

# column percentages for creating the column sum
colsum=ct3.sum(axis=0)
colpct=ct3/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs3= scipy.stats.chi2_contingency(ct3)
print (cs3)

recode4 = {0: 0, 2: 2}
sub2['COMP1v14']= sub2['Alcoholuse'].map(recode4)

# contingency table of observed counts
ct4=pandas.crosstab(sub2['Income'], sub2['COMP1v14'])
print (ct4)

# column percentages for creating the column sum
colsum=ct4.sum(axis=0)
colpct=ct4/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs4= scipy.stats.chi2_contingency(ct4)
print (cs4)
