import requests
from bs4 import BeautifulSoup

url = 'http://www.mainflow.in'

response = requests.get(url)


if response.status_code == 200:
   
    page_content = response.content
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")
print(soup)


page_text = soup.get_text()
print("Page Text:")
print(page_text)


links = soup.find_all('a', href=True)
print("\nLinks:")
for link in links:
    print(link['href'])

images = soup.find_all('img', src=True)
print("\nImages:")
for image in images:
    print(image['src'])
