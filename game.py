from asyncio.windows_events import NULL
from distutils.command.sdist import show_formats
from tkinter import *
from tkinter.tix import CELL, TEXT
from turtle import st
import enum

class GameStatusEnum(enum.Enum):
    NOT_END = 1
    PLAYER1_WIN = 2
    PLAYER1_LOSE = 3
    DRAW = 4

window = Tk()

IMG_PLAY = PhotoImage(file = "./assets/btn-play.png") # Lade ein Bild aus Computer
IMG_QUIT = PhotoImage(file = "./assets/btn-quit.png")
IMG_BACKGROUND = PhotoImage(file = "./assets/background.png")
IMG_PLAYER1 = PhotoImage(file = "./assets/btn-1player.png")
IMG_PLAYER2 = PhotoImage(file = "./assets/btn-2players.png")
IMG_GO = PhotoImage(file = "./assets/btn-start.png")
IMG_CELL = PhotoImage(file = "./assets/cell.png")
IMG_INTERFACE = PhotoImage(file = "./assets/interface.png")
IMG_NEWGAME = PhotoImage(file = "./assets/btn-newgame.png")
IMG_MENU = PhotoImage(file = "./assets/btn-menu.png")
SYMBOL_X = PhotoImage(file = "./assets/cross.png")
SYMBOL_O = PhotoImage(file = "./assets/nought.png")

numberOfPlayers = 0 # Anzahl der Spieler
playerName1 = StringVar()
playerName2 = StringVar()
gameStatus = GameStatusEnum.NOT_END
player1inTurn = None
gameMessage = None
textGameMessage = None
gameArea_canvas = None
gameBoard = [[0,0,0],[0,0,0],[0,0,0]]
# 0 = leer, 1 = SYMBOL_X, 2 = SYMBOL_O

def close():
    window.quit()

def showStartScreen():
    window.geometry("641x742") # Größe des Fensters
    window.configure(bg = "#ffffff")
    window.resizable(False, False) # Legt fest, ob das Fenster skalierbar ist

    canvas = Canvas(
        window,
        bg = "#ffffff", # Hintergrundfarbe
        height = 742,
        width = 641,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    btnPlay = Button(
        image = IMG_PLAY,
        borderwidth = 0,
        highlightthickness = 0,
        command = showPlayingScreen,
        relief = "flat")

    btnPlay.place(
        x = 180, y = 240,
        width = 281,
        height = 79)

    btnQuit = Button(
        image = IMG_QUIT,
        borderwidth = 0,
        highlightthickness = 0,
        command = close,
        relief = "flat")

    btnQuit.place(
        x = 180, y = 423,
        width = 281,
        height = 79)

    canvas.create_image(
        318.0, 375.0,
        image=IMG_BACKGROUND)


def showPlayingScreen():
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 742,
        width = 641,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    btnPlayer1 = Button(
        image = IMG_PLAYER1,
        borderwidth = 0,
        highlightthickness = 0,
        command = inputPlayerName1,
        relief = "flat")

    btnPlayer1.place(
        x = 180, y = 240,
        width = 281,
        height = 79)

    btnPlayer2 = Button(
        image = IMG_PLAYER2,
        borderwidth = 0,
        highlightthickness = 0,
        command = inputPlayerName1and2,
        relief = "flat")

    btnPlayer2.place(
        x = 180, y = 423,
        width = 281,
        height = 79)

def checkPlayer1win():
    global gameBoard
    if gameBoard[0][0] == 1 and gameBoard[0][1] == 1 and gameBoard [0][2] == 1:
        return True
    if gameBoard[1][0] == 1 and gameBoard[1][1] == 1 and gameBoard [1][2] == 1:
        return True
    if gameBoard[2][0] == 1 and gameBoard[2][1] == 1 and gameBoard [2][2] == 1:
        return True
    if gameBoard[0][0] == 1 and gameBoard[1][0] == 1 and gameBoard [2][0] == 1:
        return True
    if gameBoard[0][1] == 1 and gameBoard[1][1] == 1 and gameBoard [2][1] == 1:
        return True
    if gameBoard[0][2] == 1 and gameBoard[1][2] == 1 and gameBoard [2][2] == 1:
        return True
    if gameBoard[0][0] == 1 and gameBoard[1][1] == 1 and gameBoard [2][2] == 1:
        return True
    if gameBoard[0][2] == 1 and gameBoard[1][1] == 1 and gameBoard [2][0] == 1:
        return True
    else:
        return False

def checkPlayer2win():
    global gameBoard
    if gameBoard[0][0] == 2 and gameBoard[0][1] == 2 and gameBoard [0][2] == 2:
        return True
    if gameBoard[1][0] == 2 and gameBoard[1][1] == 2 and gameBoard [1][2] == 2:
        return True
    if gameBoard[2][0] == 2 and gameBoard[2][1] == 2 and gameBoard [2][2] == 2:
        return True
    if gameBoard[0][0] == 2 and gameBoard[1][0] == 2 and gameBoard [2][0] == 2:
        return True
    if gameBoard[0][1] == 2 and gameBoard[1][1] == 2 and gameBoard [2][1] == 2:
        return True
    if gameBoard[0][2] == 2 and gameBoard[1][2] == 2 and gameBoard [2][2] == 2:
        return True
    if gameBoard[0][0] == 2 and gameBoard[1][1] == 2 and gameBoard [2][2] == 2:
        return True
    if gameBoard[0][2] == 2 and gameBoard[1][1] == 2 and gameBoard [2][0] == 2:
        return True
    else:
        return False

def checkGameNotEnd(): # Überprüft, ob das Spiel noch läuft
    global gameBoard
    for row in range(0,3):
        for col in range(0,3):
            if gameBoard[row][col] == 0:
                return True
    return False

def inputPlayerName1():
    global numberOfPlayers
    numberOfPlayers = 1
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 742,
        width = 641,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    canvas.create_text(
        226.5, 310,
        text = "Your Name:",
        fill = "#000000",
        font = ("Arial", int(12.0)))

    btn_Go = Button(
        image = IMG_GO,
        borderwidth = 0,
        highlightthickness = 0,
        command = startPlaying,
        relief = "flat")

    btn_Go.place(
        x = 180, y = 459,
        width = 281,
        height = 79)

    global playerName1

    textBoxPlayername1 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        textvariable = playerName1,
        highlightthickness = 0)

    textBoxPlayername1.place(
        x = 306, y = 299,
        width = 215.0,
        height = 34)

def inputPlayerName1and2():
    global numberOfPlayers
    numberOfPlayers = 2
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 742,
        width = 641,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    btn_showGameArea = Button(
        image = IMG_GO,
        borderwidth = 0,
        highlightthickness = 0,
        command = showGameArea,
        relief = "flat")

    btn_showGameArea.place(
        x = 180, y = 459,
        width = 281,
        height = 79)

    canvas.create_text(
        192.4, 202,
        text = "Player 1:",
        fill = "#000000",
        font = ("None", int(23.0)))

    canvas.create_text(
        192.4, 305,
        text = "Player 2:",
        fill = "#000000",
        font = ("None", int(23.0)))

    global playerName1

    textBoxPlayername1 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        textvariable = playerName1,
        highlightthickness = 0)

    textBoxPlayername1.place(
        x = 306.0, y = 189,
        width = 215.0,
        height = 34)

    textPlayerName2 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        textvariable = playerName2,
        highlightthickness = 0)

    textPlayerName2.place(
        x = 306.0, y = 292,
        width = 215.0,
        height = 34)

def getPlayer2Name():
    global numberOfPlayers
    if numberOfPlayers == 1:
        return "Computer"
    if numberOfPlayers == 2:
        return playerName2.get()

def startPlaying():
    print('Start playing')
    global playerName1
    global player1inTurn
    global gameStatus
    player1inTurn = True
    showGameArea()

def refreshGameMessage():
    global gameMessage
    global player1inTurn
    global playerName1
    global gameStatus
    if gameStatus == GameStatusEnum.DRAW:
        gameMessage = "It's a draw"
    elif gameStatus == GameStatusEnum.PLAYER1_WIN:
        gameMessage = "You win! Congrats!"
    elif gameStatus == GameStatusEnum.PLAYER1_LOSE:
        gameMessage = "You lose :'("
    else:
        if (player1inTurn):
            gameMessage = f"{playerName1.get()}'s turn!"
        else:
            gameMessage = f"{getPlayer2Name()}'s turn!"

    print('refreshGameMessage')
    print(gameMessage)

def createCellClickHandler(row, col):
    def OnClick():
        global gameBoard
        global player1inTurn
        global gameStatus
        if gameStatus != GameStatusEnum.NOT_END:
            print('GAME END°!')
            return
        cellValue = gameBoard[row][col]
        if cellValue != 0:
            return
        elif player1inTurn:
            gameBoard[row][col] = 1
            player1inTurn = False
            refreshGameBoard()
        else:
            gameBoard[row][col] = 2
            player1inTurn = True
            refreshGameBoard()
        print('------------')
        print(gameBoard)
    return OnClick

def showCell(row, col):
    global gameBoard
    cellImage = IMG_CELL
    cellValue = gameBoard[row][col]
    if cellValue == 1:
        cellImage = SYMBOL_X
    elif cellValue == 2:
        cellImage = SYMBOL_O
    cell = Button(
        image = cellImage,
        borderwidth = 0,
        highlightthickness = 0,
        command = createCellClickHandler(row, col),
        relief = "flat")

    x0 = 242
    y0 = 174
    w = 140
    h = 140
    gap = 31

    cell.place(
        x = x0 + col*(gap + w), 
        y = y0 + row*(gap + h),
        width = 140,
        height = 140)

def refreshGameStatus():
    global gameStatus
    if checkPlayer1win():
        gameStatus = GameStatusEnum.PLAYER1_WIN
    elif checkPlayer2win():
        gameStatus = GameStatusEnum.PLAYER1_LOSE
    elif checkGameNotEnd():
        pass
    else:
        gameStatus = GameStatusEnum.DRAW

    print('refreshGamestatus')
    print(gameStatus)

# Dieses Funktion aktualisiert das gameBoard
def refreshGameBoard():
    global textGameMessage
    global gameArea_canvas
    global gameMessage

    refreshGameStatus()

    refreshGameMessage()
            
    gameArea_canvas.itemconfig(textGameMessage, text=gameMessage)
    for row in range(0,3):
        for col in range(0,3):
            showCell(row, col)

def clearBoard():
    global gameBoard
    for row in range(0,3):
        for col in range(0,3):
            gameBoard[row][col] = 0

def resetGame():
    global gameStatus
    clearBoard()
    gameStatus = GameStatusEnum.NOT_END
    refreshGameBoard()

def gotoMenu():
    resetGame()
    showStartScreen()

def showGameArea():
    global playerName1
    global playerName2
    global numberOfPlayers
    global gameArea_canvas

    window.geometry("966x742")
    window.configure(bg = "#ffffff")
    gameArea_canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 742,
        width = 966,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    gameArea_canvas.place(x = 0, y = 0)

    btn_GotoMenu = Button(
        image = IMG_MENU,
        borderwidth = 0,
        highlightthickness = 0,
        command = gotoMenu,
        relief = "flat")

    btn_GotoMenu.place(
        x = 641, y = 15,
        width = 100,
        height = 35)

    btn_Newgame = Button(
        image = IMG_NEWGAME,
        borderwidth = 0,
        highlightthickness = 0,
        command = resetGame,
        relief = "flat")

    btn_Newgame.place(
        x = 801, y = 15,
        width = 137,
        height = 35)

    gameArea_canvas.create_text(
        125.5, 274.0,
        text = playerName1.get(),
        fill = "#000000",
        font = ("None", int(23.0)))

    player2 = ""
    if (numberOfPlayers == 2):
        player2 = playerName2.get()
    else:
        player2 = "Computer"

    gameArea_canvas.create_text(
        845.5, 274.0,
        text = player2,
        fill = "#000000",
        font = ("None", int(23.0)))

    gameArea_canvas.create_text(
        125.0, 493.5,
        text = 0,
        fill = "#000000",
        font = ("None", int(23.0)))

    gameArea_canvas.create_text(
        846.0, 493.5,
        text = 0,
        fill = "#000000",
        font = ("None", int(23.0)))

   
    global textGameMessage
    textGameMessage = gameArea_canvas.create_text(
        483.0, 119.0,
        text = gameMessage,
        fill = "#000000",
        font = ("Inter-Regular", int(36.0)))

    gameArea_canvas.create_image(483, 371, image=IMG_INTERFACE)

     # Zeige das Spielfeld an
    refreshGameBoard()

showStartScreen()

window.mainloop()
