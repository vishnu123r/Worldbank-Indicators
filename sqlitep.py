from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

engine = create_engine('sqlite:///E:\Mission\Personal project\World bank Indicators\database.sqlite')
print(engine.table_names())

df = pd.read_sql_query("SELECT IndicatorCode, CountryCode, Value, Year FROM Indicators WHERE CountryCode == 'CHN'", engine)

df_china_tertiary = df.loc[df.IndicatorCode == 'SE.TER.ENRR', ['Value', 'Year']]
df_china_GDP = df.loc[df.IndicatorCode == 'NY.GDP.PCAP.KN', ['Value', 'Year']]



lst = [(r['Year'], r['Value'], r1['Value'])  for i,r in df_china_GDP.iterrows() for i1,r1 in df_china_tertiary.iterrows() if r['Year'] == r1['Year'] ]

df_plot = pd.DataFrame(lst, columns = ['Year', 'GDP Value', 'Tertiary' ])


col = [random.choice(['red', 'blue', 'green','yellow']) for _ in range(41)]
df_plot.plot.scatter(x = 'Year', y = 'Tertiary', s= (np.array(df_plot.loc[:, 'GDP Value']))/75, c= col, alpha=0.5 )
plt.yticks([5,10,15,20,25,30],['5%', '10%', '15%','20%','25%','30%'])
plt.show()

