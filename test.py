import requests
from bs4 import BeautifulSoup
import re
import time

# Connects to lichess game
url = 'https://lichess.org/QMlF41dq'

buffer_list = []

while True:

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    coords_list = []
    # scrapes for all piece data
    pieces = soup.select('piece')

    for piece in pieces:
        coordinates = piece.get('style')
        coords = re.findall(r'\d+\.\d+', coordinates)
        float_coords = [(float(coords[i]), float(coords[i+1])) for i in range(0, len(coords), 2)]

        # converts percentages into ints 0-7 and place pieces on the grid
        for position in float_coords:
            row, col = position
            int_coords = (int(row / 12.5), int(col / 12.5))
            
            coords_list.append(int_coords)                

    if buffer_list is None:
        buffer_list = coords_list.copy()


    for tuple1, tuple2 in zip(coords_list, buffer_list):
            if tuple1 != tuple2:
                print(tuple1, tuple2)

    buffer_list = coords_list.copy()
    time.sleep(0.1)
