def show_records():
    
    with open("records.txt", encoding="utf-8") as records:
        in_test = records.read()
    
    # úprava dat dle rozdělovače
    pointer = in_test.split("|")

    # očištění dat a vložení do listu ke zpracování
    list_from_text = [clear for clear in pointer if clear != "" and clear != "\n"]

    # grafický přehled rekordů
    tabulka = """+---------------------------------------------+
|                   RECORDS                   |
+----------+------------------------+---------+
| POSITION | PLAYER     | TIME      | ROUND\S |
+----------+------------------------+---------+"""
    print(tabulka)

    # vloží list_from_text do fce ke zpracování a vypíše do tabulky
    max_hodnota = 0
    for position, list in enumerate(lists_to_list3(list_from_text), 1):
        max_hodnota += 1 
        print(
            f"| {position:^8} |", f"{list[0]:<10} |", f"{list[1]:>9} |", f"{list[2]:>7} |"
            )
        if max_hodnota == 15:
            break
    print("+---------------------------------------------+")


def lists_to_list3(list_from_text: list) -> list:
    """Funkce udělá listy v listu -> [[player, time, round],...]
    a seřadí od nejlepšího dosaženého času.
    """
    lists_in_list = []
    stop = 0
    while stop != len(list_from_text):
        
        lists_in_list.append([ list_from_text[0 + stop], list_from_text[1 + stop], list_from_text[2 + stop]])
        stop += 3

    lists_in_list.sort(key=lambda listx3: listx3[1])

    return lists_in_list


# slouží k zablokování automatického spuštění volané fce v případě kdy je v souboru, ze kterého importujeme fce spuštěna (tady ne - muselo by -> show_records() <- být v kódu records.py ^)
# if __name__ == "__main__":
#     show_records()