import requests
from bs4 import BeautifulSoup

url = "https://www.chess.com/game/live/83361366559"
login_url = "https://www.chess.com/login_check"

login_data = {
    "username": "hjbvrnwebkjhglG",
    "_password": "Qw$DgM5u5v$T6QK"
}
# start a session
session = requests.Session()
# post the login data to the login url
login_response = session.post(login_url, data=login_data)
# get the url while logged in
response = session.get(url)
# print the response content
soup = BeautifulSoup(response.content, "html.parser")
elements = soup.select('[class*="piece"]')

if __name__ == '__main__':
    for element in elements:
        print(element)
