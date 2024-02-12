from bs4 import BeautifulSoup
import requests

domain = 'https://www.fungipedia.org'
url = domain + '/hongos/abortiporus-biennis.html'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664'
headers = {'User-Agent': user_agent}
session = requests.Session()
response = session.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

for item in soup.select('.sigProLinkWrapper a[href]:not([href=""])'):
    print(domain + item.attrs.get('href'))