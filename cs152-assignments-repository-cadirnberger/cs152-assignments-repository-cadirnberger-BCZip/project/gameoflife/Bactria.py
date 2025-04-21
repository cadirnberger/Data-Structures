
from datastructures.array2d import Array2D

class Bactria():
    def __init__(self):
        self._new_world = Array2D.empty(5, 5, bool)
        self._current_rows = rows
        self._current_colums = colums
    def game_function(self):
        amount_of_cells = 0
        for row in range(len(self._new_world)):
            for col in range(len(self._new_world[row])):
                if self._new_world[row][col]:
                      amount_of_cells +=1
                if row < self._current_rows-1:
                    if self._new_world[row+1][col]:
                        amount_of_cells +=1
                if col < self._current_colums-1:
                    if self._new_world[row][col+1]:
                        amount_of_cells +=1
                if self._new_world[row-1][col]:
                    amount_of_cells +=1
                if self._new_world[row][col-1]:
                    amount_of_cells +=1
                if amount_of_cells > 2:
                    print('X', end = ' ')
                    self._new_world[row][col] = True
                else:
                    print('-', end = ' ')
                    self._new_world[row][col] = False
                amount_of_cells = 0
            print()
        print()