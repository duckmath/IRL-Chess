import requests
from bs4 import BeautifulSoup

url = "https://www.chess.com/game/live/83361366559"#input("Enter the URL: ")
#print("The URL is: " + url)
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
#elements = soup.find_all(class_="piece bn square-78")
elements = soup.select('[class*="piece"]')
for element in elements:
    print(element)
if __name__ == '__main__':
    print("hi")
#https://www.chess.com/login_check
#username=hjbvrnwebkjhglG&_password=Qw%24DgM5u5v%24T6QK&login=&_target_path=https%3A%2F%2Fwww.chess.com%2F&_token=098c22.5eAjhRHmqEUZe8UKs8Zb30tTC-bsJap6U4d4UnhEa_o.l5BK8kic-QIuOuhs8PM8uAF-b5S1Tvk8Yc0aJBEhJI_IqE7kRYvaIiAfjA

