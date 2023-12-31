#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 12:51:23 2022

@author: dimitardimitrov
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import kruskal
from scipy.stats import ttest_rel
from scipy.stats import normaltest
from scipy.stats import iqr
from statistics import median
from statistics import mean
import statsmodels.api as statsmodels
import matplotlib.transforms as transforms
import scikit_posthocs as sp



DataFile="Rapa tub aS PFF.xlsx"
Xlabel1='C'
Xlabel2='αSp'
Xlabel3='αSpR'

Ylabel="Synapse tubulin (norm.)"


#symbols :  α, β


SaveAs='Rapa tub aS PFF.png'
Columns=[0,1,2]
fig_dims = (1.2, 1.8)
yaxisrange=0,3
fontsz = 8
fontzszannot= 8
StatTest=kruskal


#Global parameters>>>>>>>>>>>>>>>>>>>>>>>>>>
sns.set(rc={"figure.dpi":300, 'savefig.dpi':1200})  
sns.set_theme(style="ticks")
fig, ax = plt.subplots(figsize=fig_dims)

# DATA files<<<<<<<<<<<<<<<<<<

df = pd.read_excel(DataFile, usecols=Columns) 
df=[df[col].dropna() for col in df]

def SaveFile(): 
    fig.savefig(SaveAs,
                format='png', bbox_inches='tight', pad_inches=0.07) 
    
#figure components arrangement
g=sns.boxplot(data=df, width=0.38, 
            boxprops={'zorder': 2, 'facecolor':'#999999', 'edgecolor': "k","linewidth": 1},
            medianprops={'zorder': 3, 'color': "k","linewidth": 1},
            whiskerprops={'zorder': 4, 'color': "k","linewidth": 1},
            capprops={'zorder': 5, 'color': "k","linewidth": 1},
            showfliers = False)



g=sns.stripplot(data=df, palette=['#003366','#003366','#003366'], size=2, ax=g,zorder=3,  alpha=1)
offset = transforms.ScaledTranslation(3/72., 0, ax.figure.dpi_scale_trans)
trans = ax.collections[0].get_transform()
ax.collections[0].set_transform(trans + offset)
ax.collections[1].set_transform(trans + offset)
ax.collections[2].set_transform(trans + offset)


g.tick_params(labelsize=9, pad=0.2, length=2)
g.axes.autoscale(axis='y', tight=False)
ax.set_ylim(0.7)
#g.axes.set_ylim(yaxisrange)
g.axes.set_ylabel(Ylabel, fontsize = fontsz, labelpad=1)
sns.despine (top=True, right=True)
#g.axes.set_title(PlotTitle, fontsize= fontsz, pad=1) #SAVE AS PLOT TITLE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 

g.set_xticks([0,1,2])
g.set_yticks([0,1,2,3])
nobs=str(df[0].value_counts().sum())
nobs2=str(df[1].value_counts().sum())
nobs3=str(df[2].value_counts().sum())



g.set_xticklabels([Xlabel1, Xlabel2, Xlabel3], fontsize=fontsz)
#g.text(x=0, y=0.95, s=nobs, color='k', fontsize=7, horizontalalignment='center')
#g.text(x=1, y=0.95, s=nobs2,  color='k', fontsize=7, horizontalalignment='center')
#g.text(x=2, y=0.95, s=nobs3,  color='k', fontsize=7, horizontalalignment='center')

# Stats<<<<<<<<<<<<<<<<<<<<<<<<<<<<

pvalueStat= StatTest(df[0],df[1],df[2]).pvalue
dunn= sp.posthoc_dunn(df, p_adjust = 'holm')


#‘bonferroni’ : one-step correction 
#‘sidak’ : one-step correction ‘holm-sidak’ : step-down method using Sidak adjustments 
#‘holm’ : step-down method using Bonferroni adjustments 
#‘simes-hochberg’ : step-up method (independent) 
#‘hommel’ : closed method based on Simes tests (non-negative) 
#‘fdr_bh’ : Benjamini/Hochberg (non-negative) 
#‘fdr_by’ : Benjamini/Yekutieli (negative) 
#‘fdr_tsbh’ : two stage fdr correction (non-negative) 
#‘fdr_tsbky’ : two stage fdr correction (non-negative)




if pvalueStat >= 0.05:
        symbol = "p=%.2f" % pvalueStat
if pvalueStat < 0.05:
            symbol = "p=%.2f" % pvalueStat
if pvalueStat < 0.01:
                symbol = "p=%.3f" % pvalueStat
if pvalueStat < 0.001:
        symbol = 'p<0.001'
if pvalueStat < 0.0001:
        symbol = 'p<0.0001'



g.axes.set_title(symbol, fontsize= fontsz, color="white", pad=1) #SAVE AS PLOT TITLE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#plt.grid(which='major', axis='y') 

med1=median(df[0])
med2=median(df[1])
med3=median(df[2])


iqr1=iqr(df[0])
iqr2=iqr(df[1])
iqr3=iqr(df[2])

#norm1=normaltest(df[0]).pvalue
#norm2=normaltest(df[1]).pvalue
#norm3=normaltest(df[2]).pvalue

print(Ylabel)
print(Xlabel1)
print(Xlabel2)
print(Xlabel3)

print("N:")
print(nobs)
print(nobs2)
print(nobs3)

print("normality:")
#print(norm1)
#print(norm2)
#print(norm3)
print("median:")
print(med1)
print(med2)
print(med3)

print("IQR:")
print(iqr1)
print(iqr2)
print(iqr3)

print("Stats")
print(StatTest)
print(pvalueStat)
print("Dunn posthoc:")
print(dunn)

dfhead=pd.DataFrame(df)
print(dfhead.head(2))

plt.show(g)


Save = input('Save file? y/n')
if Save in ['y']:
    fig = g.figure 
    SaveFile()
    print ("Yay! Saved!")
else:
    print ("Not saved!")

