import gdelt
import csv
import pandas as pd
import datetime

gd2 = gdelt.gdelt(version=2)
d1 = datetime.date(2017, 1, 2)
d2 = datetime.date(2017, 1, 10)
frames = []
days = [d1 + datetime.timedelta(days=x) for x in range((d2-d1).days + 1)]
for day in days:
    day1 = str(day.strftime('%Y %m %d'))
    results1 = gd2.Search(date = day1, table='events', output='pandas dataframe')
    frames.append(results1)
results = pd.concat(frames)
df = pd.DataFrame(data=results)
df = df[['ActionGeo_CountryCode','EventBaseCode', 'Year']]
df = df.loc[df['EventBaseCode'] == "141"]
df2 = df
df3 = df2.groupby(['Year','ActionGeo_CountryCode', 'EventBaseCode']).size().reset_index()
df3.rename(columns = {0: 'Summa'}, inplace = True)
print(df3)
