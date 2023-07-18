import requests
from bs4 import BeautifulSoup
import time


url = "https://www.chess.com/game/9b5454d7-2584-11ee-a1b4-9d2e7001000f"
login_url = "https://www.chess.com/login_check"

login_data = {
    "username": "hjbvrnwebkjhglG",
    "_password": "Qw$DgM5u5v$T6QK"
    # what does the token mean?
    # may have to switch to live chess.
}


class Piece:
    def __init__(self, type, location, color):
        self.type = type
        self.location = location
        self.color = color

    def __str__(self):
        return f"{self.type} {self.location} is {self.color}"

    class Location:
        def __init__(self, col, row):
            self.col = col
            self.row = row

        def __str__(self):
            return f"col: {self.col}, row: {self.row}"


# start a session
session = requests.Session()


#
# pieces = {"pawn": "x", "rook": "r", "knight": "k", "bishop": "b", "king": "k", "queen": "q"}


# post the login data to the login url
# login_response = session.post(login_url, data=login_data)
# print(login_response.status_code)


def live_loop():
    # get the url while logged in

    response = session.get(url)
    if response.status_code != 200:
        quit()
    # print the response content
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.select('[class*="piece"]')
    if len(elements) == 0:
        return "No elements found"
    for i, element in enumerate(elements):
        if i != 0:
            # gets each element's classes (each should have 3) they are a piece, what piece they are, and location
            # print(element["class"])
            color = element["class"][1]
            location = element["class"][2].replace('square-', '')
            item = Piece(color[1], Piece.Location(int(location[0]) - 1, int(location[1]) - 1), color[0])
            print(str(item))
            # how can I create a place to put these pieces?
            # how can I make it so that it updates the board?

    return "Success"


if __name__ == '__main__':
    while True:
        live_loop()
        time.sleep(1)
