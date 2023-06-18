import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.worldometers.info/world-population/population-by-country/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find('table', {'id':'example2'}).find('tbody').find_all('tr')

print(len(rows))


countries_list = []

for row in rows:
    dic = {}

    dic['Country'] = row.find_all('td')[1].text
    dic['Population 2020'] = row.find_all('td')[2].text
    dic['Yearly Change'] = row.find_all('td')[3].text
    dic['Net Change'] = row.find_all('td')[4].text
    dic['Density'] = row.find_all('td')[5].text
    dic['Land Area'] = row.find_all('td')[6].text
    dic['Migrant'] = row.find_all('td')[7].text


    countries_list.append(dic)


df_countries_list = pd.DataFrame(countries_list)
df_countries_list

writer = pd.ExcelWriter('Countries_Data.xlsx')

df_countries_list.to_excel('Countries_Data.xlsx', index=False)
df_countries_list.to_csv('Countries_Data.csv', index=False)