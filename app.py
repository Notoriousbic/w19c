import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
# Create a new Player called player starting at position 3,2

board = gameboard.GameBoard()
player = player.Player(3,2)
while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    # TODO
    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!
    if (selection == "w"):
        board.checkMove(player.rowPosition - 1, player.columnPosition)
        player.moveUp()
        # board.checkMove()
    elif(selection == "s"):
        board.checkMove(player.rowPosition + 1, player.columnPosition)
        player.moveDown()
        #board.checkMove()
    elif(selection == "a"):
        board.checkMove(player.rowPosition, player.columnPosition - 1)
        player.moveLeft()
        #board.checkMove()
    elif(selection == "d"):
        board.checkMove(player.rowPosition, player.columnPosition + 1)
        player.moveRight()
    if board.checkWin(player.rowPosition, player.columnPosition):
        print("You win!")
        break
