import requests
from bs4 import BeautifulSoup

data = requests.get(
    "https://www.flipkart.com/search?q=onr%20plus&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")


soup = BeautifulSoup(data.text, 'html.parser')
phone_name = soup.find_all(name='a', class_="s1Q9rs")
price = soup.find_all(name='div', class_="_30jeq3")
data_dam = []
for i, j in zip(phone_name, price):
    m = i.get('title')
    n = j.text
    data_dam.append({'name': m, 'price': n})
# for i in price:
#     print(i.text)
#     break
print(data_dam)
