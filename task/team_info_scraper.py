from bs4 import BeautifulSoup
import requests

url = "https://kodeinkgp.in/teams"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

heads = soup.find_all(attrs={"class": "member head"})
founders = soup.find_all(attrs={"class": "founder member"})
members = soup.find_all(attrs={"class": "member"})

print(req.content)

print(heads)
print(founders)
print(members)