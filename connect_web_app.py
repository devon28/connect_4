from flask import *
from flask import g
from connect import *
import random
from random import choice
from pymongo import *

app = Flask(__name__)
client = MongoClient('127.0.0.1', 27018)
db = client.ship_database
coordinates = db.coordinates
board_width = 4
board_height = 3


      

@app.route('/') 
def root():
       global grid, turn
       grid = initialiseGrid()
       turn = initialiseTurn()
       return render_template('main.html', grid=grid, turn=turn)

@app.route('/row_one', methods = ["POST"])
def add_mark1():
       global turn  
       if checkValid(1, grid) == False:
              return render_template('main.html', grid=grid, turn=turn)
       turn = add_piece(1, grid, turn)
      
       result =  checkWinner(grid, turn)
       if result != None:
              return render_template('won.html', result=result)
       return render_template('main.html', grid=grid, turn=turn)

@app.route('/row_two', methods = ["POST"])
def add_mark2():
       global turn  
       if checkValid(2, grid) == False:
              return render_template('main.html', grid=grid, turn=turn)
       turn = add_piece(2, grid, turn)
       result =  checkWinner(grid, turn)
       if result != None:
              return render_template('won.html', result=result)
       return render_template('main.html', grid=grid, turn=turn)

@app.route('/row_three', methods = ["POST"])
def add_mark3():
       global turn
       if checkValid(3, grid) == False:
              return render_template('main.html', grid=grid, turn=turn)  
       turn = add_piece(3, grid, turn)
       result =  checkWinner(grid, turn)
       print("\/", result, "result")
       if result != None:
              return render_template('won.html', result=result)
       return render_template('main.html', grid=grid, turn=turn) 

@app.route('/row_four', methods = ["POST"])
def add_mark4():
       global turn  
       if checkValid(4, grid) == False:
              return render_template('main.html', grid=grid, turn=turn)
       turn = add_piece(4, grid, turn)
       result =  checkWinner(grid, turn)
       print("\/", result, "result")
       if result != None:
              return render_template('won.html', result=result)
       return render_template('main.html', grid=grid, turn=turn)

@app.route('/row_five', methods = ["POST"])
def add_mark5():
       global turn  
       if checkValid(5, grid) == False:
              return render_template('main.html', grid=grid, turn=turn)
       turn = add_piece(5, grid, turn)
       result =  checkWinner(grid, turn)
       if result != None:
              return render_template('won.html', result=result)
       return render_template('main.html', grid=grid, turn=turn)

@app.route('/row_six', methods = ["POST"])
def add_mark6():
       global turn  
       if checkValid(6, grid) == False:
              return render_template('main.html', grid=grid, turn=turn)
       turn = add_piece(6, grid, turn)
       result =  checkWinner(grid, turn)
       if result != None:
              return render_template('won.html', result=result)
       return render_template('main.html', grid=grid, turn=turn)

@app.route('/row_seven', methods = ["POST"])
def add_mark7():
       global turn  
       if checkValid(7, grid) == False:
              return render_template('main.html', grid=grid, turn=turn)
       turn = add_piece(7, grid, turn)
       result =  checkWinner(grid, turn)
       print("\/", result, "result")
       if result != None:
              return render_template('won.html', result=result)
       return render_template('main.html', grid=grid, turn=turn)


@app.route('/calculate', methods = ["POST"])
def calculate():
       global won       
       data = request.form
       
       X = data['X']
       Y = data['Y']
       if validateRow(X) and validateCol(Y):

              xy_coord = { "X": X, "Y": Y }
              coordinates.insert_one(xy_coord)
              won = checkResult(grid, int(X), int(Y), ship_one, ship_two, won)

              if won:
                     return render_template('won.html', coords=list(coordinates.find({})))

       return render_template('main.html', grid=grid) 
       
         
if __name__ == '__main__':
       app.run(port = 6789, debug = True)
