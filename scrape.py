import requests
from bs4 import BeautifulSoup
import re
import time
import curses

def draw_grid(stdscr, grid):
    stdscr.clear()  # Clear the screen
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            stdscr.addstr(row, col*2, grid[row][col])
    stdscr.refresh()


grid = [[' ' for _ in range(8)] for _ in range(8)]

stdscr = curses.initscr()

curses.curs_set(0)
while True:
    # Clear the grid from previous data
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            grid[row][col] = ' '

# Connects to lichess game
    url = 'https://lichess.org/tq8WgAey'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


# scrapes for all piece data
    pieces = soup.select('piece')



    for piece in pieces:
        piece_type = piece.get('class')
        coordinates = piece.get('style')

        if coordinates:
            # Converts coordinates to float values
            coords = None
            coords = re.findall(r'\d+\.\d+', coordinates)
            float_coords = None
            float_coords = [(float(coords[i]), float(coords[i+1])) for i in range(0, len(coords), 2)]

            # converts percentages into ints 0-7 and place pieces on the grid
            for position in float_coords:
                row, col = position
                int_coords = (int(row / 12.5), int(col / 12.5))
                grid[int_coords[0]][int_coords[1]] = 'X'  

    draw_grid(stdscr, grid)

    time.sleep(0.25)
    
    stdscr.clear()

curses.endwin()
