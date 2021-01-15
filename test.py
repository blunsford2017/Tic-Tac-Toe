# Imports
# import random
# import os
# import time

# # Define board
# board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

# # Print the Header
# def print_header():
#     print("""
#         TIC - TAC - TOE! 
#         To play Tic-Tac-Toe you need to get three in a row. 
#         Your Choices are 1 to 9.
#          1 | 2 | 3 
#          4 | 5 | 6
#          7 | 8 | 9
#           """)

# # Define the print_board function
# def print_board():
#     print("   |    |  ")
#     print(" " + board[1] + " | " + board[2] + "  | " + board[3] + " ")
#     print("   |    |  ")
#     print("---|----|---")
#     print("   |    |  ")
#     print(" " + board[4] + " | " + board[5] + "  | " + board[6] + " ")
#     print("   |    |  ")
#     print("---|----|---")
#     print("   |    |  ")
#     print(" " + board[7] + " | " + board[8] + "  | " + board[9] + " ")
#     print("   |    |  ")

# # Define raw input
# choice = "Please choose an empty space for X. "

# # Define Function
# while True:
#     os.system("clear")
#     print_header()
#     print_board()

#     # choice = int("Please choose an empty space for X. ")
#     choice = int(choice)

#     # check to see if the space is empty
#     if  board[choice] == " ":
#         board[choice] = "X"
#     else:
#             print("Sorry, that space is not empty!")
#             time.sleep(1)

#     # check for X win
#     if (board[1] == "X" and board[2] == "X" and board[3] == "X"):
#         print("X wins! Congradulations")
#         break