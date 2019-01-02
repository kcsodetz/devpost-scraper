import requests
import sys
from bs4 import BeautifulSoup

if sys.argv != 2:
    print("[ERROR] Missing arguments")
    exit(99)

user = 'kcsodetz'
url = 'https://www.devpost.com/' + user
data = requests.get(url=url)
soup = BeautifulSoup(data.text, 'html.parser')

projects = soup.find('a', {'href': '/' + user}).find('span').text.strip()
hackathons = soup.find('a', {'href': '/' + user + '/challenges'}).find('span').text.strip()
followers = soup.find('a', {'href': '/' + user + '/followers'}).find('span').text.strip()
winner = soup.find_all('img', {'class': 'winner'})
print(projects, hackathons, followers, len(winner))
