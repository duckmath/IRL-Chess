import requests
from bs4 import BeautifulSoup
import re
import time
import curses
import copy





buffer_list = []

while True:
# Connects to lichess game
    url = 'https://lichess.org/QMlF41dq'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

# scrapes for all piece data
    pieces = soup.select('piece')

    coords_list = []
    changed_tuples = []
    has_changed = False # flag to check if the board has changed

    for piece in pieces:
        piece_type = piece.get('class')
        coordinates = piece.get('style')

        if coordinates:
            # Converts coordinates to float values
            coords = re.findall(r'\d+\.\d+', coordinates)
            float_coords = [(float(coords[i]), float(coords[i+1])) for i in range(0, len(coords), 2)]

            # converts percentages into ints 0-7 and place pieces on the grid
            for position in float_coords:
                row, col = position
                int_coords = (int(row / 12.5), int(col / 12.5))
                
                coords_list.append(int_coords)                

    # checks if the buffer list is empty and adds the first set of coordinates
    if buffer_list is None:
        buffer_list = coords_list.copy()

# Compare the tuples and add the changed ones to the new list
    for tuple1, tuple2 in zip(coords_list, buffer_list):
        if tuple1 != tuple2:
            changed_tuples.append((tuple1, tuple2))
            has_changed = True 
       
            
    if has_changed:
        print("change detected")
        buffer_list = coords_list.copy()

    for coord in changed_tuples:
        print(coord)


    time.sleep(0.25)

