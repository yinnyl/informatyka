from tkinter import *
import random

# sprawdzenie czy ktoś już zwyciężył
def sprawdzenie_wygranej():

# ten sam znak (tekst) w wierszu
    for wiersz in range(3):
        if buttons[wiersz][0]['text'] == buttons[wiersz][1]['text'] == buttons[wiersz][2]['text'] == 'X' or buttons[wiersz][0]['text'] == buttons[wiersz][1]['text'] == buttons[wiersz][2]['text'] == 'O':
            buttons[wiersz][0].config(bg='green')
            buttons[wiersz][1].config(bg='green')
            buttons[wiersz][2].config(bg='green')
            return True

# ten sam znak (tekst) w kolumnie
    for kolumna in range(3):
        if buttons[0][kolumna]['text'] == buttons[1][kolumna]['text'] == buttons[2][kolumna]['text'] == 'X' or buttons[0][kolumna]['text'] == buttons[1][kolumna]['text'] == buttons[2][kolumna]['text'] == 'O':
            buttons[0][kolumna].config(bg='green')
            buttons[1][kolumna].config(bg='green')
            buttons[2][kolumna].config(bg='green')
            return True

# ten sam znak (tekst) po skosie (z lewej do prawej)
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] == 'X' or buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] == 'O':
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True

# ten sam znak (tekst) po skosie (z prawej do lewej)
    elif buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] == 'X' or buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] == 'O':
        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True

# sprawdzenie czy jest remis
    elif puste_pola() is False:
        for wiersz in range(3):
            for kolumna in range(3):
                buttons[wiersz][kolumna].config(bg='grey')
        return "remis"

    else:
        return False


# przełączanie na rundę następnego gracza
def kolejny_gracz(wiersz, kolumna):
    global gracz
    if buttons[wiersz][kolumna]['text'] == '' and sprawdzenie_wygranej() is False:
        if gracz == znak_gracza[0]:
            buttons[wiersz][kolumna]['text'] = gracz

            if sprawdzenie_wygranej() is False:
                gracz = znak_gracza[1]
                label_gracz.config(text=("kolej gracza " +znak_gracza[1]))

            elif sprawdzenie_wygranej() is True:
                label_gracz.config(text=(znak_gracza[0] + " wygrał"))

            elif sprawdzenie_wygranej() == "remis":
                label_gracz.config(text="remis")

        else:
            buttons[wiersz][kolumna]['text'] = gracz

            if sprawdzenie_wygranej() is False:
                gracz = znak_gracza[0]
                label_gracz.config(text=("kolej gracza "+ znak_gracza[0]))

            elif sprawdzenie_wygranej() is True:
                label_gracz.config(text=(znak_gracza[1] + " wygrał"))

            elif sprawdzenie_wygranej() == "remis":
                label_gracz.config(text=("remis"))
    print(wiersz)
    print(kolumna)

# liczy ile pustych pól zostało
def puste_pola():
    pola = 9
    for wiersz in range(3):
        for kolumna in range(3):
            if buttons[wiersz][kolumna]['text'] != '':
                pola -= 1
    if pola == 0:
        return False
    else:
        return True

def zrestartuj_gre():
    global gracz
    gracz = random.choice(znak_gracza)
    label_gracz.config(text="kolej gracza " +gracz, font=("Helvetica", 40))
    for wiersz in range(3):
        for kolumna in range(3):
            buttons[wiersz][kolumna].config(text='')


gra = Tk()
gra.title("kółko i krzyżyk")
znak_gracza = ["X","O"]
gracz = random.choice(znak_gracza)
buttons = [['', '', ''], ['', '', ''], ['', '', '']]

label_gracz = Label(text="kolej gracza "+gracz, font=('Helvetica', 40))
label_gracz.pack(side="top")

button_restartowania = Button(text="zrestartuj grę", font=('Helvetica',20), command=zrestartuj_gre)
button_restartowania.pack(side="top")

frame = Frame(gra)
frame.pack()

for wiersz in range(3):
    for kolumna in range(3):
        buttons[wiersz][kolumna] = Button(frame, text='', font=('Helvetica', 20), width=10, height=5, command=lambda row=wiersz, column=kolumna: kolejny_gracz(wiersz, kolumna))
        buttons[wiersz][kolumna].grid(row=wiersz, column=kolumna)

gra.mainloop()