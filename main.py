import requests
from bs4 import BeautifulSoup
import time
import os
from urllib.parse import quote
from classes import Piece
from fake_useragent import UserAgent


login_url = "https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/game/bd1f0466-265b-11ee-ab8c-b284ac01000f"  # login
login_post_url = "https://www.chess.com/login_check"  # login post url
session = requests.session()  # start a session
game_url = "https://www.chess.com/game/bd1f0466-265b-11ee-ab8c-b284ac01000f"  # current game url


def login(current_game):
    global token  # sets up token as a global variable
    response = session.get(login_url, allow_redirects=True)  # gets the login url data
    soup = BeautifulSoup(response.content, "html.parser")  # parses the html
    token_input = soup.find('input', {'name': '_token'})  # finds the token
    if token_input:
        token = token_input.get('value')
        # print("Token:", token)
    else:
        print("Token not found.")

    login_data = {"_username": "jchsfkuvdiwheorv",
                  "_password": "Qw%24DgM5u5v%24T6QK",
                  "login": '',
                  "_target_path": quote(game_url),
                  "_token": token
                  }

    data_string = "&".join([f"{key}={value}" for key, value in
                            login_data.items()])  # formats the data into a string that can be sent to the server
    print(data_string)
    # login_post = session.post(login_url, data=data_string)
    headers = {
        "User-Agent": UserAgent().random,
        "Referer": login_url
    }

    # Perform the login request
    login_post = session.post(login_post_url, data=login_data, headers=headers, allow_redirects=True, verify=True)
    print(login_post.status_code)
    if login_post.status_code == 200:
        print("Login failed.")
        time.sleep(1)
        quit()

    if login_post.url == game_url:
        print("Login successful.")
    else:
        print("Login failed.")
        time.sleep(1)
        quit()


login(login_url)


def live_loop():
    # get the url while logged in
    chessboard = [['  ' for _ in range(8)] for _ in range(8)]

    response = session.get(game_url, allow_redirects=True)
    current_url = response.url
    print("Current URL:", current_url)
    if response.status_code != 200:
        print("error")
        quit()
    print(response.status_code)
    # print the response content
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.select('[class*="piece"]')
    is_logged_in = soup.select(
        '[class*="button auth login ui_v5-button-component ui_v5-button-primary login-modal-trigger"]')
    print(is_logged_in.__str__())
    # if len(is_logged_in) == 0:
    # print("Not logged in")
    print("source is", elements.__str__()[:100])

    if len(elements) == 0:
        return "No elements found"
    print("Current URL:", current_url)
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
    # print('\n' * 100) # temporary fix

    print("\n")
    for row in chessboard:
        print(row)


if __name__ == '__main__':
    while True:
        live_loop()
        time.sleep(1)
        break
