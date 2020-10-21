# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 10:27:52 2020

@author: omar.elfarouk
"""


import numpy
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi 
from pandas import DataFrame as df

data = pd.read_csv('gapminder.csv', low_memory=False)
df = pd.DataFrame(data)
#setting variables you will be working with to numeric
df = df.replace(r'\s+', 0, regex=True) #Replace empty strings with zero


#subset data to income per person , alcohol consumption ,suiside rate , and employment
sub1=data
sub1 = sub1.replace(r'\s+', 0, regex=True) #Replace empty strings with zero
#SETTING MISSING DATA


# Creating a secondary variable multiplying income by alcohol consumption by employment rate

#sub1['suicideper100th']=sub1['suicideper100th'].replace(0, numpy.nan)

sub1['suicideper100th']= pd.to_numeric(sub1['suicideper100th'])

#sub1['Income']= pd.to_numeric(sub1['Income'])
ct1 = sub1.groupby('suicideper100th').size()
print (ct1)

# using ols function for calculating the F-statistic and associated p value
model1 = smf.ols(formula='suicideper100th ~ C(Income)', data=sub1).fit() 
results1 = model1 
print (results1.summary())

sub2 = sub1[['suicideper100th', 'Income']].dropna()

print ('means for income by suicide status')
m1= sub2.groupby('Income').mean()
print (m1)

print ('standard deviations for income suiside status')
sd1 = sub2.groupby('Income').std()
print (sd1)
#i will call it sub3
sub3 = sub1[['suicideper100th', 'Alcoholuse']].dropna()

model2 = smf.ols(formula='suicideper100th ~ C(Alcoholuse)', data=sub3).fit()
print (model2.summary())

print ('means for alcohol use by suicide status')
m2= sub3.groupby('Alcoholuse').mean()
print (m2)

print ('standard deviations for alcohol use by suicide')
sd2 = sub3.groupby('Alcoholuse').std()
print (sd2)
#tuckey honesty test comparision for post hoc test
mc1 = multi.MultiComparison(sub3['suicideper100th'], sub3['Alcoholuse'])
res1 = mc1.tukeyhsd()
print(res1.summary())
