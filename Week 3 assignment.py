# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 18:24:12 2020

@author: omar.elfarouk
"""

import pandas
import numpy
import seaborn
import scipy
import matplotlib.pyplot as plt

data = pandas.read_csv('gapminder.csv', low_memory=False)

#setting variables you will be working with to numeric


data['internetuserate'] = pandas.to_numeric(data['internetuserate'], errors='coerce')
data['urbanrate'] = pandas.to_numeric(data['urbanrate'], errors='coerce')
data['incomeperperson'] = pandas.to_numeric(data['incomeperperson'], errors='coerce')


data['alcconsumption'] = pandas.to_numeric(data['alcconsumption'], errors='coerce')
data['incomeperperson'] = pandas.to_numeric(data['incomeperperson'], errors='coerce')
data['suicideper100th'] = pandas.to_numeric(data['suicideper100th'], errors='coerce')


data['incomeperperson']=data['incomeperperson'].replace(' ', numpy.nan)
data['alcconsumption']=data['alcconsumption'].replace(' ', numpy.nan)
data['suicideper100th']=data['suicideper100th'].replace(' ', numpy.nan)

#Plotting figure
#scat1 = seaborn.regplot(x="incomeperperson", y="alcconsumption", fit_reg=True, data=data)
#plt.xlabel('incomeperperson')
#plt.ylabel('Alcoholuse')
#plt.title('Scatterplot for the Association Between income per personand Alcohol usage')

#scat2 = seaborn.regplot(x="incomeperperson", y="suicideper100th", fit_reg=True, data=data)
#plt.xlabel('Income per Person')
#plt.ylabel('suicideper100th')
#plt.title('Scatterplot for the Association Between Income per Person and Suicide Rate')


scat3 = seaborn.regplot(x="alcconsumption", y="suicideper100th", fit_reg=True, data=data)
plt.xlabel('Alcohol usage')
plt.ylabel('suicideper100th')
plt.title('Scatterplot for the Association Between Alcohol usage and Suicide Rate')

#Cleaning data
data_clean=data.dropna()

#Applying pearson correlation
print ('association between Income per person and Alcohole isage')
print (scipy.stats.pearsonr(data_clean['incomeperperson'], data_clean['alcconsumption']))


print ('association between incomeperperson and suscide rate ')
print (scipy.stats.pearsonr(data_clean['incomeperperson'], data_clean['suicideper100th']))


print ('association between Alcohol usage and suscide rate ')
print (scipy.stats.pearsonr(data_clean['alcconsumption'], data_clean['suicideper100th']))