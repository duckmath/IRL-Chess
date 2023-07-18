import requests
from bs4 import BeautifulSoup
import time
import os

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


# start a session
session = requests.Session()

#
# pieces = {"pawn": "x", "rook": "r", "knight": "k", "bishop": "b", "king": "k", "queen": "q"}


# post the login data to the login url
# login_response = session.post(login_url, data=login_data)
# print(login_response.status_code)


chessboard = [['  ' for _ in range(8)] for _ in range(8)]


# print(chessboard)


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
    # sort whole list by location[row][col], then start printing from the top left to the bottom right (0,0 to 7,7)
    # not going to work as I need to constantly update the board
    # make a 8x8 grid where they can move freely (0,7) is top left, (7,0) is bottom right (maybe)
    for i, element in enumerate(elements):
        if i != 0:
            # gets each element's classes (each should have 3) they are a piece, what piece they are, and location
            # print(element["class"])
            # makes white always on bottom
            color = element["class"][1]

            if color[0] == "b":
                newcolor = "w" + color[1]
            else:
                newcolor = "b" + color[1]
            type_of_piece = color[1]
            location = element["class"][2].replace('square-', '')
            item = Piece(type_of_piece, list((int(location[1]) - 1, int(location[0]) - 1)), newcolor[0])
            chessboard[item.location[0]][item.location[1]] = item.color + item.type

            # how can I create a place to put these pieces?
            # how can I make it so that it updates the board?
    update_board(chessboard)
    return "Success"


def update_board(chessboard):
    # prints chessboard by row
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n' * 100) # temporary fix

    print("\n")
    for row in chessboard:
        print(row)


if __name__ == '__main__':
    while True:
        live_loop()
        time.sleep(1)

