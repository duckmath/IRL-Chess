import requests
from bs4 import BeautifulSoup
import time

example_list = ["a", "b", "c", "d", "e", "f", "g", "h"]

url = "https://www.chess.com/game/live/83361366559"
login_url = "https://www.chess.com/login_check"

login_data = {
    "username": "hjbvrnwebkjhglG",
    "_password": "Qw$DgM5u5v$T6QK"
    # what does the token mean?
    # may have to switch to live chess.
}
# start a session
session = requests.Session()


# post the login data to the login url
# login_response = session.post(login_url, data=login_data)
# print(login_response.status_code)


def live_loop():
    # get the url while logged in
    response = session.get(url)
    # print the response content
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.select('[class*="piece"]')
    if len(elements) == 0:
        return "No elements found"
    for i, element in enumerate(elements):
        if i != 0:
            # gets each element's classes (each should have 3) they are a piece, what piece they are, and location
            print(element.get('class'))

    return "Success"


if __name__ == '__main__':
    while True:
        live_loop()
        time.sleep(1)
        break
