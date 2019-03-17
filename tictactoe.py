__author__ = 'erenaslangiray'

board =["-","-","-","-","-","-","-","-","-","-"]
def print_board():
    print "Current board status:"
    print ("1: " + board[1]+ "  2: " +board[2] +"  3: " + board[3])
    print ("4: " + board[4]+ "  5: " +board[5] +"  6: " + board[6])
    print ("7: " + board[7]+ "  8: " +board[8] +"  9: " + board[9])

def move_1 ():
    move1 = input("Your move?(Choose a number for putting X)")
    if move1 > 0 and move1 < 10 and board[move1] == "-":
        board[move1]= "X"
    else:
        print "Wrong number choice please try again."
        move_1()

def move_2():
    move2 = input("Your move?(Choose a number for putting O)")
    if move2 > 0 and move2 < 10 and board[move2] == "-":
        board[move2]= "O"
    else:
        print "Wrong number choice please try again."
        move_2()

def move_3():
    move3 = input("Your move?(Choose a number for putting X)")
    if move3 > 0 and move3 < 10 and board[move3] == "-":
        board[move3]= "X"
    else:
        print "Wrong number choice please try again."
        move_3()

def move_4():
    move4 = input("Your move?(Choose a number for putting O)")
    if move4 > 0 and move4 < 10 and board[move4] == "-":
        board[move4]= "O"
    else:
        print "Wrong number choice please try again."
        move_4()

def move_5():
    move5 = input("Your move?(Choose a number for putting X)")
    if move5 > 0 and move5 < 10 and board[move5] == "-":
        board[move5]= "X"
    else:
        print "Wrong number choice please try again."
        move_5()

def move_6():
    move6 = input("Your move?(Choose a number for putting O)")
    if move6 > 0 and move6 < 10 and board[move6] == "-":
        board[move6]= "O"
    else:
        print "Wrong number choice please try again."
        move_6()

def move_7():
    move7 = input("Your move?(Choose a number for putting X)")
    if move7 > 0 and move7 < 10 and board[move7] == "-":
        board[move7]= "X"
    else:
        print "Wrong number choice please try again."
        move_7()

def move_8():
    move8 = input("Your move?(Choose a number for putting O)")
    if move8 > 0 and move8 < 10 and board[move8] == "-":
        board[move8]= "O"
    else:
        print "Wrong number choice please try again."
        move_8()

def move_9():
    move9 = input("Your move?(Choose a number for putting X)")
    if move9 > 0 and move9 < 10 and board[move9] == "-":
        board[move9]= "X"
    else:
        print "Wrong number choice please try again."
        move_9()

def check_for_win_x():
    if board[1] == "X" and board[2] == "X" and board[3]== "X":
        return True
    elif board[4] == "X" and board[5]== "X" and board[6] == "X":
        return True
    elif board [7] == "X" and board[8]== "X" and board[9]== "X":
        return True
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        return True
    elif board [2]== "X"and board[5]== "X" and board[8]== "X":
        return True
    elif board [3]== "X"and board[6]=="X" and board[9]=="X":
        return True
    elif board [1]== "X"and board[5]=="X"and board[9]=="X":
        return True
    elif board[3]== "X"and board[5]=="X"and board[7]=="X":
        return True
    else:
        return False

def check_for_win_o():
    if board[1] == "O" and board[2] == "O" and board[3]== "O":
        return True
    elif board[4] == "O" and board[5]== "O" and board[6] == "O":
        return True
    elif board [7] == "O" and board[8]== "O" and board[9]== "O":
        return True
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        return True
    elif board [2]== "O"and board[5]== "O" and board[8]== "O":
        return True
    elif board [3]== "O"and board[6]=="O" and board[9]=="O":
        return True
    elif board [1]== "O"and board[5]=="O"and board[9]=="O":
        return True
    elif board[3]== "O"and board[5]=="O"and board[7]=="O":
        return True
    else:
        return False

def print_board_final():
    print "Game over! Last status of the board:"
    print ("1: " + board[1]+ "  2: " +board[2] +"  3: " + board[3])
    print ("4: " + board[4]+ "  5: " +board[5] +"  6: " + board[6])
    print ("7: " + board[7]+ "  8: " +board[8] +"  9: " + board[9])

def tie_board():
    print "Game is tie! Last status of the board:"
    print ("1: " + board[1]+ "  2: " +board[2] +"  3: " + board[3])
    print ("4: " + board[4]+ "  5: " +board[5] +"  6: " + board[6])
    print ("7: " + board[7]+ "  8: " +board[8] +"  9: " + board[9])


def game():
    print "Welcome to the game!"
    player1 = raw_input ("What is the name of Player 1:")
    player2 = raw_input ("What is the name of Player 2:")
    if player1 == player2:
        player2 = player2 + "(2)"
    print player1,"represents X and", player2,"represents O."
    print player1,"plays first."
    print_board()
    move_1()
    print_board()
    move_2()
    print_board()
    move_3()
    print_board()
    move_4()
    print_board()
    move_5()
    if check_for_win_x() == True :
        print "Congratulations",player1,"has won!"
        print_board_final()
        return
    else:
        print_board()
    move_6()
    if check_for_win_o() == True :
        print "Congratulations",player2,"has won!"
        print_board_final()
        return
    else:
        print_board()
    move_7()
    if check_for_win_x() == True :
        print "Congratulations",player1,"has won!"
        print_board_final()
        return
    else:
        print_board()
    move_8()
    if check_for_win_o() == True :
        print "Congratulations",player2,"has won!"
        print_board_final()
        return
    else:
        print_board()
    move_9()
    if check_for_win_x() == True :
        print "Congratulations",player1,"has won!"
        print_board_final()
        return
    else:
        tie_board()





game()