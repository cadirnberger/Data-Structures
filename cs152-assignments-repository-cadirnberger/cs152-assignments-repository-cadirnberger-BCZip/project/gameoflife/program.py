import random
import time
from datastructures.array2d import Array2D
from datastructures.iarray import IArray
from project.gameoflife.kbhit import KBHit
from project.gameoflife.World import World


                

class main():
    print('Welcome to game of life')

    rows = int(input('Enter rows: '))
    colums = int(input('Enter colums: '))
    max_evolution = int(input('Enter max evolution: '))
    speed = int(input('Enter speed: '))
    world = World(rows, colums, max_evolution, speed)
    world.run()


if __name__ == '__main__':
    main()