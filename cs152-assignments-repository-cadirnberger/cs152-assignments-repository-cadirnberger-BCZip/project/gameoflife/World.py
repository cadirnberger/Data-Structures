import random
import time
from datastructures.array2d import Array2D
from datastructures.iarray import IArray
from project.gameoflife.kbhit import KBHit
from project.gameoflife.Bactria import Bactria



class World():  
    def __init__(self, rows, colums, max_evolution, speed):
        self._current_rows = rows
        self._current_colums = colums
        self._current_max_evolution = max_evolution
        self._speed = speed
        self._current_world = Array2D.empty(rows, colums, bool)
        self._current_world: list[list[bool]] = []
        self._new_world = Array2D.empty(rows, colums, bool)
        self._change = False
        for r in range(rows):
            self._current_world.append([False] * colums)
        for row in range(rows):
            for col in range(colums):
                self._current_world[row][col] = random.choice((True, False))



    def print_current_world(self):
        for row in range(len(self._current_world)):
            for col in range(len(self._current_world[row])):
                print_value = 'X' if self._current_world[row][col] else '-'
                print(print_value, end = ' ')
            print()
        print()
    def run(self) -> None:
       # bactria = Bactria()
        kb = KBHit()
        print('Press S to start the current world (To stop the program press S again): ')
        while True:
            if  kb.kbhit():
                key = kb.getch()
                if key == 's':
                    print(key)
                    time.sleep(2)
                    self.start_animation()
                    print()
                    break
    def count_neighbors(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self._current_rows and 0 <= c < self._current_colums:
                count += self._current_world[r][c]
        return count
    def game_function(self):
        self._change = False
        for row in range(self._current_rows):
            for col in range(self._current_colums):
                neighbors = self.count_neighbors(row, col)
                if neighbors == 3:
                 self._new_world[row][col] = True
                elif neighbors == 2:
                 self._new_world[row][col] = self._current_world[row][col]
                 self._change = True
                else:
                 self._new_world[row][col] = False
    def start_animation(self):
        evolution_count = 0
        kb = KBHit()
        while evolution_count < self._current_max_evolution:
            self.game_function()
            self.print_current_world()
            evolution_count += 1
            time.sleep(self._speed)
            if not self._change:
                print('Not Enough Bactria... Shuting Down Program')
                break
            elif Array2D(self._current_world) == self._new_world:
                print('Stable Bactria... Shuting Down Program')
                break
            elif  kb.kbhit():
                key = kb.getch()
                if key == 's':
                    print('Stopping The Program')
                    break
            elif evolution_count == self._current_max_evolution:
                print('Max Evolution...Shuting Down Program')
            else:
                for row in range(self._current_rows):
                    for col in range(self._current_colums):
                        self._current_world[row][col] = self._new_world[row][col]