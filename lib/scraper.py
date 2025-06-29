# from turtle import ht
# from bs4 import BeautifulSoup
# import requests

# headers = {'user-agent': 'my-app/0.0.1'}
# html = requests.get("https://flatironschool.com/", headers=headers)
from bs4 import BeautifulSoup
import requests

headers = {"user-agent": "my-app/0.0.1"}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, "html.parser")

headings = doc.select(".heading-financier")

for heading in headings:
    print(heading.get_text(strip=True))
