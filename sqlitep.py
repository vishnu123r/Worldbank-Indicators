from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random

engine = create_engine('sqlite:///E:\Mission\Personal project\World bank Indicators\database.sqlite')
print(engine.table_names())

df = pd.read_sql_query("SELECT IndicatorCode, CountryCode, Value, Year FROM Indicators WHERE IndicatorCode == 'SL.UEM.TOTL.ZS'", engine)

#df_china_tertiary = df.loc[df.IndicatorCode == 'SE.TER.ENRR', ['Value', 'Year']]
#df_china_GDP = df.loc[df.IndicatorCode == 'NY.GDP.PCAP.KN', ['Value', 'Year']]

df_GDP_2014 = df.loc[df.Year == 2014, ['Value','CountryCode']]

df_plot = df_GDP_2014.loc[:, 'Value'].values
x = len(df_plot)
sqrt_x = np.sqrt(x)
n_bins = int(sqrt_x)

sns.set()

#plot histogram
plt.hist(df_plot,bins = n_bins)
_ = plt.ylabel('Count')
_ = plt.xlabel('Unemployment rate')
#_ = plt.xticks(np.arange(0,3.5*10**7,0.5*10**7), ['0','5M','10M','15M','20M','25M','30M','35M'])
plt.show()

#plot ECDF plot
sorted_ = np.sort(df_plot)
yvals = np.arange(len(sorted_))/float(len(sorted_))
plt.plot(sorted_, yvals, marker = '.', linestyle = 'none')
_ = plt.xlabel('Unemployment rate')
#_ = plt.xticks(np.arange(0,3.5*10**7,0.5*10**7), ['0','5M','10M','15M','20M','25M','30M','35M'])
_ = plt.ylabel('ECDF')
percentiles = np.array([25,50,75])
medians = np.percentile(df_GDP_2014['Value'], percentiles)
plt.plot(medians, percentiles/100, marker = 'D', linestyle = 'none', color = 'red' )
plt.show()
#boxplot 
sns.boxplot(y = 'Value', data = df_GDP_2014)

plt.show()
#lst = [(r['Year'], r['Value'], r1['Value'])  for i,r in df_china_GDP.iterrows() for i1,r1 in df_china_tertiary.iterrows() if r['Year'] == r1['Year'] ]

#df_plot = pd.DataFrame(lst, columns = ['Year', 'GDP Value', 'Tertiary' ])


#col = [random.choice(['red', 'blue', 'green','yellow']) for _ in range(41)]
#df_plot.plot.scatter(x = 'Year', y = 'Tertiary', s= (np.array(df_plot.loc[:, 'GDP Value']))/75, c= col, alpha=0.5 )
#plt.yticks([5,10,15,20,25,30],['5%', '10%', '15%','20%','25%','30%'])
#plt.show()

