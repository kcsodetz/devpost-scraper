import requests
import sys
from bs4 import BeautifulSoup

FAIL = '\033[91m'
WARN = '\033[93m'
NC = '\033[0m'

if len(sys.argv) != 2:
    print(FAIL + "[ERROR] Missing argument `username`\n")
    print(NC + "Usage: python3 scraper.py `username`\n")
    exit(99)

user = sys.argv[1]
url = 'https://www.devpost.com/' + user
data = requests.get(url=url)

if data.status_code != 200:
    print(FAIL + "[ERROR] 404 Error, cannot find username {}".format(WARN + user))
    exit(99)

soup = BeautifulSoup(data.text, 'html.parser')

projects = soup.find('a', {'href': '/' + user}).find('span').text.strip()
hackathons = soup.find('a', {'href': '/' + user + '/challenges'}).find('span').text.strip()
followers = soup.find('a', {'href': '/' + user + '/followers'}).find('span').text.strip()
winner = soup.find_all('img', {'class': 'winner'})

print("Projects:\t{}\nHackathons:\t{}\nFollowers:\t{}\nWins:\t\t{}".format(projects, hackathons, followers, len(winner)))

