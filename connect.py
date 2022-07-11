import random
import copy
#ship_one_result = False
#ship_two_result = False
global ship_one_result, ship_two_result
from connect_web_app import *


def initialiseGrid():
    grid = [["O"] * 7] * 6  #4 rows by 5 columns grid for battleship
    for i in range(6):      #to avoid aliasing
        grid[i] = ["O"] * 7
    return grid

def initialiseTurn():  
    turn = "red"    
    return turn



def displayGrid(grid):
    for row in grid:
        print("\t".join(row))
    print()

def validateRow(row):
    if not row.isdigit(): #presence and type check
        return False
    if int(row) < 0 or int(row) > 3: #range check
        return False
    return True

def validateCol(col):
    if not col.isdigit(): #presence and type check
        return False
    if int(col) < 0 or int(col) > 4: #range check
        return False
    return True

def checkResult(grid, row, col, ship_one, ship_two, won):
    ship_one_result = False
    ship_two_result = False

    ship_one_rows = [ship_one[0][0], ship_one[1][0]]
    ship_one_columns = [ship_one[0][1], ship_one[1][1]]

    ship_two_rows = [ship_two[0][0], ship_two[1][0], ship_two[2][0]]
    ship_two_columns = [ship_two[0][1], ship_two[1][1], ship_two[2][1]]

    if row in ship_one_rows and col in ship_one_columns:
        grid[row][col] = "Hit"
    elif row in ship_two_rows and col in ship_two_columns:
        grid[row][col] = "Hit"
    else:
         grid[row][col] = "X" #player guessed wrongly

    if ship_one_result != True:
        for i in range(len(ship_one_rows)):
            if grid[ship_one_rows[i]][ship_one_columns[i]] != "Hit":
                return
        ship_one_result = True

    if ship_two_result != True:
        for i in range(len(ship_two_rows)):
            if grid[ship_two_rows[i]][ship_two_columns[i]] != "Hit":
                return
        ship_two_result = True

    if ship_one_result == True and ship_two_result == True:
        won = True
    return won

def add_piece(column, grid, turn):
    column = column -1 
    for i in reversed(range(6)):
        if grid[i][column] == "O":
            grid[i][column] = turn
            if turn == "red":
                turn = "blue"
            else:
                turn = "red"
            print(turn, "\n")
            return turn


def checkWinner(grid, turn):
    if turn == "red":
        turn = "blue"
    else:
        turn = "red"
    for i in reversed(range(6)):
        for k in reversed(range(7)):
            if grid[i][k] == turn:
                #up
                if i>=3:
                    count = 0
                    for j in reversed(range(i-3, i+1)):
                        if grid[j][k] == turn:
                            count += 1
                    if count == 4:
                        return turn
                # side
                if k >= 3:
                    count = 0
                    for j in reversed(range(k-3, k+1)):
                        if grid[i][j] == turn:
                            count += 1
                    if count == 4:
                        return turn
                #up left
                if k >=3 and i >= 3:
                    count = 0
                    for j in range(4):
                        if grid[i-j][k-j] == turn:
                            count += 1
                    if count == 4:
                        return turn
                # up right
                if i >= 3 and k <= 3:
                    count = 0
                    for j in range(4):
                        if grid[i-j][k+j] == turn:
                            count += 1
                    if count == 4:
                        return turn 
    return None


def checkValid(column, grid):
    column -= 1
    count = 0
    for i in range(6):
        if grid[i][column] != "O":
            count += 1
    if count + 1 <= 6:
        return True
    return False

def checkWinner1(grid, turn):
    player = copy.deepcopy(turn) 
    for i in reversed(range(6)):
        for k in reversed(range(7)):
            #red
            if grid[i][k] == player:
                #up
                count = 1
                for j in range(i-3, i+1):
                    if grid[j][k] == player:
                        
                        count += 1
                        
                
                    if count == 4:
                        return player
                """#up right diagnnal
                count = 1
                if k <= 3 and i <= 2:              # index in bounds
                    for j in range(4):
                        if grid[k+j][i+j] == turn:
                            count += 1
                        if count == 4:
                            return turn
                # up left diagonal
                count = 1
                if k >= 3 and i <= 2:
                    for j in range(4):
                        if grid[k+j][i-j] == turn:
                            count += 1
                        if count == 4:
                            return turn
                # side ways
                count += 1
                if k <= 3:
                    for j in range(4):
                        if grid[i][k+j] == turn:
                            count += 1
                        if count == 4:
                            return turn"""
        return None

                
                    

           
    

    