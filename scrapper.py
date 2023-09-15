from os import name
from bs4 import BeautifulSoup
import requests 
try:
    source = requests.get('https://www.skysports.com/la-liga-table')
    source.raise_for_status()
    soup = BeautifulSoup(source.text,'html.parser')
    teams = soup.find('tbody').find_all('tr',class_="standing-table__row")
    
    for team in teams:
        name = team.find('td',class_="standing-table__cell standing-table__cell--name").a.text
        
        print(team)


    
except Exception as e:
 print(e)



