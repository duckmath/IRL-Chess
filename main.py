import requests
from bs4 import BeautifulSoup

url = "https://www.chess.com/play/computer"#input("Enter the URL: ")
#print("The URL is: " + url)
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
#elements = soup.find_all(class_="piece bn square-78")
elements = soup.select('[class*="piece"]')
for element in elements:
    print(element)
if __name__ == '__main__':
    print("hi")

