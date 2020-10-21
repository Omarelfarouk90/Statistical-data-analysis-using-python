# -*- Week4 assignment-*-
"""
Created on Sun Aug 16 12:57:52 2020

@author: omar.elfarouk
"""

#%%

# Using gap minder data 

# CORRELATION
import pandas
import numpy
import scipy.stats
import seaborn
import matplotlib.pyplot as plt

data = pandas.read_csv('gapminder.csv', low_memory=False)

data['alcconsumption'] = pandas.to_numeric(data['alcconsumption'], errors='coerce')
data['incomeperperson'] = pandas.to_numeric(data['incomeperperson'], errors='coerce')
data['suicideper100th'] = pandas.to_numeric(data['suicideper100th'], errors='coerce')

data['incomeperperson']=data['incomeperperson'].replace(' ', numpy.nan)

data['alcconsumption']=data['alcconsumption'].replace(' ', numpy.nan)

data['suicideper100th']=data['suicideper100th'].replace(' ', numpy.nan)

data_clean=data.dropna()

print (scipy.stats.pearsonr(data_clean['alcconsumption'], data_clean['suicideper100th']))

def incomegrp (row):
   if row['incomeperperson'] <= 1000:
      return 1
   elif row['incomeperperson'] <= 5000:
      return 2
   elif row['incomeperperson'] > 9000:
      return 3
   
data_clean['incomegrp'] = data_clean.apply (lambda row: incomegrp (row),axis=1)

chk1 = data_clean['incomegrp'].value_counts(sort=False, dropna=False)
print(chk1)

sub1=data_clean[(data_clean['incomegrp']== 1)]
sub2=data_clean[(data_clean['incomegrp']== 2)]
sub3=data_clean[(data_clean['incomegrp']== 3)]

print ('association between Alcohol consumption and suicide rate for LOW income countries')
print (scipy.stats.pearsonr(sub1['alcconsumption'], sub1['suicideper100th']))
print ('       ')
print ('association between urbanrate and internetuserate for MIDDLE income countries')
print (scipy.stats.pearsonr(sub2['alcconsumption'], sub2['suicideper100th']))
print ('       ')
print ('association between urbanrate and internetuserate for various income among countries')
print (scipy.stats.pearsonr(sub3['alcconsumption'], sub3['suicideper100th']))
#%%
scat1 = seaborn.regplot(x="alcconsumption", y="suicideper100th", data=sub1)
plt.xlabel('Alchol consumption ')
plt.ylabel('Suicide rate')
plt.title('Scatterplot for the Association Between Alcohol consumption and Suicide rate for LOW income countries')
print (scat1)
#%%
scat2 = seaborn.regplot(x="alcconsumption", y="suicideper100th", fit_reg=False, data=sub2)
plt.xlabel('Alcohol consumption')
plt.ylabel('Suicide rate')
plt.title('Scatterplot for the Association Between Alcohol consumption and Suicide Rate for MIDDLE income countries')
print (scat2)
#%%
scat3 = seaborn.regplot(x="alcconsumption", y="suicideper100th", data=sub3)
plt.xlabel('Alcohol consumption')
plt.ylabel('Suicide rate')
plt.title('Scatterplot for the Association Between Alcohol consumption and Suicide rate for various  income countries')
print (scat3)
