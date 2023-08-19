import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu
from scipy.stats import iqr
from scipy.stats import normaltest
from scipy.stats import sem
from statistics import median
from statistics import mean
import matplotlib.transforms as transforms

DataFile = "taupff  wb.xlsx"
Xlabel1 = 'Control'
Xlabel2 = 'T pff'
Ylabel = "Total Tau/Actin (norm.)"
SaveAs = 'taupff  wb.png'
Columns = [0, 1]
fig_dims = (0.8, 1.4)
yaxisrange = (0,2)
fontsz = 7
fontszasterix=10
fontszannot = 7
StatTest = mannwhitneyu

# Symbols:  α, 

# Set figure and axis parameters
sns.set(rc={"figure.dpi": 300, 'savefig.dpi': 1200})
sns.set_theme(style="ticks")
fig, ax = plt.subplots(figsize=fig_dims)

# Read data from Excel file
df = pd.read_excel(DataFile, usecols=Columns)
df = [df[col].dropna() for col in df]

def SaveFile():
    fig.savefig(SaveAs, format='png', bbox_inches='tight', pad_inches=0.07)

# Plot boxplot and stripplot
g=sns.barplot(data=df, zorder=0,edgecolor='none', color='grey', errcolor="grey")
g = sns.stripplot(data=df,palette=['#003366','#003366'], size=2, ax=g, zorder=6)
offset = transforms.ScaledTranslation(3.8 / 72., 0, ax.figure.dpi_scale_trans)
trans = ax.collections[0].get_transform()
ax.collections[0].set_transform(trans + offset)
ax.collections[1].set_transform(trans + offset)

# Set plot parameters
g.tick_params(labelsize=7, pad=0.2, length=2)
g.axes.set_ylim(yaxisrange)
g.axes.set_ylabel(Ylabel, fontsize=fontsz, labelpad=1)
sns.despine(top=True, right=True)
g.set_xticks([0, 1])
g.set_yticks([0, 1,2])
nobs = str(df[0].value_counts().sum())
nobs2 = str(df[1].value_counts().sum())
g.set_xticklabels([Xlabel1, Xlabel2], fontsize=fontsz)

# Perform statistical test
pvalueStat = StatTest(x=df[0], y=df[1]).pvalue
y_max1 = max(df[1])
y_offset1 = 0.2 / 25.4 * y_max1  # 5 mm converted to inches

# Add annotations to indicate the significance level and which pair is being compared
if pvalueStat < 0.001:
    g.axes.annotate("***", xy=(1, y_max1 + y_offset1), xytext=(1, y_max1 + y_offset1),
                     ha='center', va='center', color='k', fontsize=fontszasterix,
                     arrowprops=dict(arrowstyle="-", lw=1.5), annotation_clip=False)
elif 0.001 <= pvalueStat < 0.01:
    g.axes.annotate("**", xy=(1, y_max1 + y_offset1), xytext=(1, y_max1 + y_offset1),
                     ha='center', va='center', color='k', fontsize=fontszasterix,
                     arrowprops=dict(arrowstyle="-", lw=1.5), annotation_clip=False)
elif 0.01 <= pvalueStat < 0.05:
    g.axes.annotate("*", xy=(1, y_max1 + y_offset1), xytext=(1, y_max1 + y_offset1),
                     ha='center', va='center', color='k', fontsize=fontszasterix,
                     arrowprops=dict(arrowstyle="-", lw=1.5), annotation_clip=False)
else:
    g.axes.annotate("ns", xy=(1, y_max1 + y_offset1), xytext=(1, y_max1 + y_offset1),
                     ha='center', va='center', color='k', fontsize=7,
                     arrowprops=dict(arrowstyle="-", lw=1.5), annotation_clip=False)

# Calculate and print statistics
mean1 = mean(df[0])
mean2 = mean(df[1])
sem1=sem(df[0])
sem2=sem(df[1])


print(Ylabel)
print(Xlabel1)
print(Xlabel2)
print("N:")
print(nobs)
print(nobs2)
print("Stats")
print(StatTest)
print(pvalueStat)
print("Mean")
print(mean1)
print(mean2)
print("SEM")
print(sem1)
print(sem2)

# Display the plot
plt.show(g)

# Save the plot if desired
Save = input('Save file? y/n')
if Save in ['y']:
    SaveFile()
    print("Yay! Saved!")
else:
    print("Not saved!")
fontszasterix