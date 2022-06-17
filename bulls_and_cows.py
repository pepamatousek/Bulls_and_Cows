"""
bulls_and_cows.py: Druhý projekt do Engeto Online Python Akademie
K tomuto souboru je zapotřebí records.txt, který je umístěn spolu s tímto souborem.

author: Josef Matoušek
email: jmatousek.jobs@icloud.com
discord: Crazroz#8593
"""

from random import choice
from os import system
import datetime
import platform


from records import show_records


def do_separator(width: int) -> str:
    separator = "-"*width
    return separator


def which_platform():

    if platform.system() == "Windows":
        command = "cls"

    elif platform.system() == "Darwin":
        command = "clear"

    elif platform.system() == "Linux":
        command = "clear"

    else:
        command = "clear"

    return command


def first_screen(separator: str):
    print(
        f"{separator}",
        f"Welcome in the game Bulls and Cows".center(len(separator)),
        f"{separator}",
        f"Write player name:",
        f"{separator}",
        sep="\n"
        )


def player_name(command: str, separator: str) -> str:
    system(command)
    first_screen(separator)

    # kontrola zadaného vstupu
    while True:
        host = input(">>> ")

        # nedovolený znak, který slouží jako rozdělovač v records.txt
        if "|" in host:
            system(command)
            first_screen(separator)
            print('"|" is forbidden symbol...')
        
        # jméno hráče musí mít 3 až 10 znaků
        elif len(host) <= 10 and len(host) >= 3:
            players_name = host
            break
        else:
            system(command)
            first_screen(separator)
            print("It has to have 3 to 10 symbols...")

    return players_name


def menu_screen(players_name: str, separator: str):
    print(
    f"{separator}",
    f"Hi {players_name}!",
    f"I've generated a random 4 digit number for you.\nLet's play a Bulls and Cows game.",
    f"{separator}",
    f"- for start input [s]", 
    f"- for records input [r]",     
    f"- for exit input [q]",
    f"{separator}",
    sep="\n"
    )


def menu(players_name: str, command: str, separator: str): 
    system(command)
    menu_screen(players_name, separator)
    host = input(">>> ")

    # kontrola vstupu
    while True:
        if host == "s" or host == "r" or host == "q":
            break
        else:
            system(command)
            menu_screen(players_name, separator)
            print(f"Bad input...")
            host = input(">>> ")

    # spuštění výběru
    if host == "s":
        system(command)
        main_game(players_name, separator, command)

    elif host == "r":
        system(command)
        show_records()
        print(f"- for back to menu input [b]")
        host = input(">>> ")
        
        while host != "b":
            system(command)
            show_records()
            print(
                f"- for back to menu input [b]",
                f"Bad input...",
                sep="\n"
                )
            host = input(">>> ")
        
        if host == "b":
            menu(players_name, command, separator)

    elif host == "q":
        quit()


def player_input_screen(players_name: str, separator: str):
        print(
        f"{separator}",
        f"Hi {players_name}!",
        f"I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.",
        f"{separator}",
        f"Enter a number:",
        f"{separator}",
        sep="\n"
        )


def check_player_input(host: str) -> str:

    while True:

        # ověření číselného stringu
        if not host.isnumeric():
            print("Input has to be numeric...")
        # ověření prvního znaku (že není "0")
        elif host[0] == "0":
            print('Number can not start by "0"')
        # ověření počtu znaků čtyři
        elif not len(host) == 4:
            print("Please enter number with four digits...")
        # ověření unikátnosti cifer v čísle
        elif check_numerals(host):
            print("Digits have to be unique...")
        # když je vstup v pořádku
        else:
            break
        host = input(">>> ")

    return host


def check_numerals(host: str) -> bool:
    """Funkce která ověří jedinečnost čísel."""
    for number in host:
        if host.count(number) != 1:
            check = True
            break
        else:
            check = False
    return check


def generator_secret_number(number_of_digits: int) -> str:
    """Generuje str s náhodnými čísly do max. pocet_mist 10,
    číslo nezačíná nulou a číslice se neopakují.
    """

    secret_number = ""

    # cyklus generování
    while number_of_digits != 0:
        generator = choice(range(0, 10))
        secret_number += str(generator)

        # když je první číslo "0" začne od znovu
        if secret_number[0] == "0":
            secret_number = ""

        # když se číslice opakuje, tak ji odebere a začne znova
        elif secret_number.count(str(generator)) == 2:
            secret_number = secret_number[:-1]

        # když uživatel zadá parametr mimo rozsah
        elif number_of_digits > 10 or number_of_digits < 0:
            secret_number = "Range has to be between 0 to 10"
            break

        # je-li vše splněno, sníží rozsah cyklu
        else:
            number_of_digits -= 1

    # vrací tajné číslo
    return secret_number


def check_plural(bull: int, cow: int , round: int) -> list:
    # ošetření množného čísla cow/cows a bull/bulls
    if bull != 1 and cow != 1:
        bull_text = "bulls"
        cow_text = "cows"
        
    elif bull != 1:
        bull_text = "bulls"
        cow_text = "cow"

    elif cow != 1:
        cow_text = "cows"
        bull_text = "bull"

    else:
        bull_text = "bull"
        cow_text = "cow"

    # ošetření množného čísla ROUND:/ROUNDS:
    if round != 1:
        round_text = "ROUNDS:"
    
    else:      
        round_text = "ROUND:"
    
    return [bull_text, cow_text, round_text]


def main_game(players_name: str, separator: str, command: str):  
   
    player_input_screen(players_name, separator)

    secret_number = generator_secret_number(4)
    # print(secret_number)

    # spuštění časomíry
    start = datetime.datetime.now()

    # počítadlo kol
    round = 0

    # cyklus vyhodnocující/srovnávající vstup uživatele s tajným číslem
    while True:
        
        host = input(">>> ")
        cow = 0
        bull = 0
        # ověřuje uživatelský vstup a vyhodnocuje cow/bull
        for index, number in enumerate(check_player_input(host)):

            # přičte cow, když je číslo ve vstupu a nemá společný index s hádaným číslem
            if number in secret_number and number != secret_number[index]:
                cow += 1

            # přičte bull, když má číslo společný index s hádaným číslem
            elif number == secret_number[index]:
                bull += 1

        # počítadlo kol
        round += 1

        # informuje uživatele v průběhu hry o vývoji hry
        if bull < 4:
        
            # průběžný čas
            actual = datetime.datetime.now()
            time_progres = actual - start

            print(
                f"{bull} {check_plural(bull, cow, round)[0]}, {cow} {check_plural(bull, cow, round)[1]}",
                f"{separator}",
                f"PLAYER: {players_name}, {check_plural(bull, cow, round)[2]} {round}, ACTUAL TIME: {str(time_progres)[2:-3]}",
                f"{separator}",
                sep="\n"
                )

        # v případě výhry
        elif bull == 4:

            # konečný čas
            konec = datetime.datetime.now()
            time = konec - start

            # zobrazí výsledek
            win_screen(separator, players_name, bull, cow, round, time)

            # uloží výsledek hry
            save_game(players_name, time, round)
            break
    menu_after_game(players_name, command, separator, bull, cow, round, time)


def win_screen(separator: str, players_name: str, bull: int, cow: int, round: int, time):
    print(
    f"{separator}",
    f"YOUR VICTORY!".center(len(separator)),
    f"{separator}",
    f"CORRECT, you've guessed the right number\nin {round} guesses! Your finish time is {str(time)[2:-3]}.",
    f"{separator}",
    f"PLAYER: {players_name}, {check_plural(bull, cow, round)[2]} {round}, FINISH TIME: {str(time)[2:-3]}",
    f"{separator}",
    f"- for new game input [n]",
    f"- for record input [r]",
    f"- for exit input [q]",
    sep="\n"
    )


def save_game(players_name: str, time, round: int):
    victory = f"|{players_name}|{str(time)[2:-3]}|{round}|\n"
    with open ("records.txt", mode="a", encoding="utf-8") as test:
        test.write(victory)


def menu_after_game(players_name: str, command: str, separator: str, bull: int, cow: int, round: int, time):
    
    host = input(">>> ")
    
    while True:
        if host == "n" or host == "r" or host == "q":
            break
        else:
            system(command)
            win_screen(separator, players_name, bull, cow, round, time)
            print(f"Bad input...")
            host = input(">>> ")

    if host == "n":
        game()
    elif host == "r":
        system(command)
        show_records()
        print(f"- for back to menu input [b]")
        host = input(">>> ")
        
        while host != "b":
            system(command)
            show_records()
            print(
                f"- for back to menu input [b]",
                f"Bad input...",
                sep="\n"
                )
            host = input(">>> ")
        
        if host == "b":
            menu(players_name, command, separator)
    elif host == "q":
        quit()

    
def game():
    separator = do_separator(54)
    command = which_platform()
    players_name = player_name(command, separator)
    menu(players_name, command, separator)


game()