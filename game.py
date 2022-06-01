from asyncio.windows_events import NULL
from distutils.command.sdist import show_formats
from tkinter import *
from tkinter.tix import CELL, TEXT
from turtle import st

window = Tk()

IMG_PLAY = PhotoImage(file = "./assets/btn-play.png") # Lade ein Bild aus Computer
IMG_QUIT = PhotoImage(file = "./assets/btn-quit.png")
IMG_BACKGROUND = PhotoImage(file = "./assets/background.png")
IMG_PLAYER1 = PhotoImage(file = "./assets/btn-1player.png")
IMG_PLAYER2 = PhotoImage(file = "./assets/btn-2players.png")
IMG_GO = PhotoImage(file = "./assets/btn-start.png")
TEXTBOX = PhotoImage(file = "./assets/img-textbox.png")
IMG_CELL = PhotoImage(file = "./assets/cell.png")
IMG_INTERFACE = PhotoImage(file = f"./assets/interface.png")
IMG_NEWGAME = PhotoImage(file = f"./assets/btn-newgame.png")
IMG_MENU = PhotoImage(file = f"./assets/btn-menu.png")

numberOfPlayers = 0
playerName1 = StringVar()
playerName2 = StringVar()

def close():
    window.quit()

def showStartScreen():
    window.geometry("641x742") # Größe des Fensters
    window.configure(bg = "#ffffff")
    window.resizable(True, True) # Legt fest, ob das Fenster skalierbar ist

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

def showGameArea():
    global playerName1
    global playerName2
    global numberOfPlayers

    window.geometry("966x742")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 742,
        width = 966,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    btn_ShowStartScreen = Button(
        image = IMG_MENU,
        borderwidth = 0,
        highlightthickness = 0,
        command = showStartScreen,
        relief = "flat")

    btn_ShowStartScreen.place(
        x = 641, y = 15,
        width = 100,
        height = 35)

    btn_Newgame = Button(
        image = IMG_NEWGAME,
        borderwidth = 0,
        highlightthickness = 0,
        command = None,
        relief = "flat")

    btn_Newgame.place(
        x = 801, y = 15,
        width = 137,
        height = 35)

    canvas.create_text(
        125.5, 274.0,
        text = playerName1.get(),
        fill = "#000000",
        font = ("None", int(23.0)))

    player2 = ""
    if (numberOfPlayers == 2):
        player2 = playerName2.get()
    else:
        player2 = "Computer"

    canvas.create_text(
        845.5, 274.0,
        text = player2,
        fill = "#000000",
        font = ("None", int(23.0)))

    canvas.create_text(
        125.0, 493.5,
        text = 0,
        fill = "#000000",
        font = ("None", int(23.0)))

    canvas.create_text(
        846.0, 493.5,
        text = 0,
        fill = "#000000",
        font = ("None", int(23.0)))

    # Zeige das Spielfeld an
    cell1_1 = Button(
        image = IMG_CELL,
        borderwidth = 0,
        highlightthickness = 0,
        command = None,
        relief = "flat")

    cell1_1.place(
        x = 242, y = 174,
        width = 140,
        height = 140)

    cell1_2 = Button(
        image = IMG_CELL,
        borderwidth = 0,
        highlightthickness = 0,
        command = None,
        relief = "flat")

    cell1_2.place(
        x = 413, y = 174,
        width = 140,
        height = 140)

    cell1_3 = Button(
        image = IMG_CELL,
        borderwidth = 0,
        highlightthickness = 0,
        command = None,
        relief = "flat")

    cell1_3.place(
        x = 584, y = 174,
        width = 140,
        height = 140)

    cell2_1 = Button(
        image = IMG_CELL,
        borderwidth = 0,
        highlightthickness = 0,
        command = None,
        relief = "flat")

    cell2_1.place(
        x = 242, y = 345,
        width = 140,
        height = 140)

    cell2_2 = Button(
        image = IMG_CELL,
        borderwidth = 0,
        highlightthickness = 0,
        command = None,
        relief = "flat")

    cell2_2.place(
        x = 413, y = 345,
        width = 140,
        height = 140)

    cell2_3 = Button(
        image = IMG_CELL,
        borderwidth = 0,
        highlightthickness = 0,
        command = None,
        relief = "flat")

    cell2_3.place(
        x = 584, y = 345,
        width = 140,
        height = 140)

    cell3_1 = Button(
        image = IMG_CELL,
        borderwidth = 0,
        highlightthickness = 0,
        command = None,
        relief = "flat")

    cell3_1.place(
        x = 242, y = 516,
        width = 140,
        height = 140)

    cell3_2 = Button(
        image = IMG_CELL,
        borderwidth = 0,
        highlightthickness = 0,
        command = None,
        relief = "flat")

    cell3_2.place(
        x = 413, y = 516,
        width = 140,
        height = 140)

    cell3_3 = Button(
        image = IMG_CELL,
        borderwidth = 0,
        highlightthickness = 0,
        command = None,
        relief = "flat")

    cell3_3.place(
        x = 584, y = 516,
        width = 140,
        height = 140)

    canvas.create_text(
        483.0, 119.0,
        text = "counter",
        fill = "#000000",
        font = ("Inter-Regular", int(36.0)))

    canvas.create_image(483, 371, image=IMG_INTERFACE)


showStartScreen()

window.mainloop()
