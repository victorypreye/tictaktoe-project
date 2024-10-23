
import os
import random


def print_board(board):
    print("curent board:")
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
    
test_board = [' '] * 10
print_board(test_board)

def player_choice():
    player = input("Please choose your player ['player1' or 'player2']: ")
    marker = input("Please choose your marker ['X' or 'O']: ")
    if player in ["player1", "player2"] and marker.upper() in ['X', 'O']:
        return player, marker.upper()
    else:
        print("Invalid player or marker input. Please try again.")

def place_marker(board, marker, position):
 if board[position] == ' ':
     board[position] =  marker
     return True
 else:
     return False

def win_check(board, mark):
    return(
        (board[7] == mark  and board[8] == mark  and board[9] == mark) or
        (board[4] == mark  and board[5] == mark  and board[6] == mark) or
        (board[1] == mark  and board[2] == mark  and board[3] == mark) or
        (board[7] == mark  and board[4] == mark  and board[1] == mark) or
        (board[8] == mark  and board[5] == mark  and board[2] == mark) or
        (board[9] == mark  and board[6] == mark  and board[3] == mark) or
        (board[1] == mark  and board[5] == mark  and board[9] == mark) or
        (board[7] == mark  and board[5] == mark  and board[3] == mark)
    )   

def random_choose(player1, player2):
  return random.choice([player1, player2])

def space_check(board, position):
    return board[position] == " "

def check_board(board):
   for i in range(1,10):
        if space_check(board, i):
            return False
   return  True

def next_position(board, current_player):
    while True:
     position = int(input(f"please {current_player} choose your position (1-9): "))
     if position in range(1, 10) and space_check(board, position):
         return position
     else:
         print("position is already taken, Please try again.")
    
def replay():
    while True:
        choice = input("Do you want to play again ? Enter Yes or No: ")
        if choice in ['yes','no']:
            return choice == 'yes'
        else:
            print("invalid input, please enter 'Yes' or 'No' .")

def header():
    print("Welcome to Tic-Tac-Toe game\n")


def refresh_screen():
    os.system("cls")

header()

while True:
    theBoard = [' '] * 10
    player1, marker1 = player_choice()
    player2 = 'player2' if player1 == 'player1' else 'player1'
    marker2 = 'O' if marker1 == 'X' else 'X'
    refresh_screen()
    current_player = random_choose(player1, player2)
    current_player, current_marker = (player2, marker2) if current_player == player1 else (player1, marker1)
    current_marker = marker1 if current_player == player1 else marker2
    print(f"{player2} this {marker2} your marker")

    
    print(f"{current_player} will go first!")
    game_on = True

    while game_on:
        print_board(theBoard)
        print(f"{current_player}'s turn now.")
        position = next_position(theBoard, current_player)
        place_marker(theBoard, current_marker, position)
        refresh_screen()
        if win_check(theBoard, current_marker):
            print_board(theBoard)
            print(f"Congratulations,  {current_player} wins!")
            game_on = False
        elif check_board(theBoard):
            print_board(theBoard)
            print("It's a draw! Well played, both!")
            game_on = False
            
        if current_player == player1:
         current_player, current_marker = player2, marker2
        else:
         current_player, current_marker = player1, marker1

    if not replay():
        print("Thanks for playing! Goodbye!")
        break