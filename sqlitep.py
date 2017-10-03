from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

engine = create_engine('sqlite:///E:\Mission\Personal project\World bank Indicators\database.sqlite')
print(engine.table_names())

df = pd.read_sql_query("SELECT IndicatorCode, CountryCode, Value, Year FROM Indicators WHERE CountryCode == 'CHN'", engine)
#df = pd.read_sql_query("SELECT IndicatorName, IndicatorCode, CountryCode FROM Indicators WHERE Year = 2012", engine)


print(df.head())
print(df.loc([0], [0]))

df_china_tertiary = df[df['IndicatorCode'] == 'SE.TER.ENRR']
df_china_GDP = df[df['IndicatorCode'] == 'NY.GDP.PCAP.KN']
#df_china.to_csv('Indicatorcode to name.csv', index=False, encoding='utf-8')

#df_plot = df_china_tertiary.iloc([0])
#print(df_plot().head())

#plt.plot(df_china_tertiary[:, 'Value'], df_china_tertiary[:, 'Year'], )
#plt.plot(df[:, 'Value'])

