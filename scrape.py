import requests
from bs4 import BeautifulSoup

# Connects to lichess game
url = 'https://lichess.org/g2OZpcyT'  

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# scrapes for all piece data
pieces = soup.select('piece')


for piece in pieces:
    piece_type = piece.get('class')
    coordinates = piece.get('style')

    if coordinates:
        print(coordinates)

    if piece_type:
        print(piece_type)



