from tkinter import *

window = Tk()

IMG_PLAY = PhotoImage(file = f"./btn-play.png") # Lade ein Bild aus Computer
IMG_QUIT = PhotoImage(file = f"./btn-quit.png")
IMG_BACKGROUND = PhotoImage(file = f"./background.png")

def btn_clicked():
    print("Button Clicked")

def close():
    window.quit()

def btnPlayClicked():
    showPlayingScreen()

def initWindow():
    window.geometry("641x742") # Größe des Fensters
    window.configure(bg = "#ffffff")
    window.resizable(False, False) # Legt fest, ob das Fenster skalierbar ist

def showStartScreen():
    canvas = Canvas(
        window,
        bg = "#ffffff",
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
        command = btnPlayClicked,
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

    background = canvas.create_image(
        318.0, 375.0,
        image=IMG_BACKGROUND)


def showPlayingScreen():
    canvas = Canvas(
        window,
        bg = "#ff0000",
        height = 742,
        width = 641,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    Button(borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat").place(x = 180, y = 423, width = 281, height = 79)

initWindow()
showStartScreen()

window.mainloop()
