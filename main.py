import colorama
import time
import secrets
from random import randint
from datetime import datetime
from tabulate import tabulate

# Farben
GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
RED = colorama.Fore.RED
WHITE = colorama.Fore.WHITE

BTC_VALUE = 28858.20

transactions = []


class Transaction:
    def __init__(self, timestamp, amount, transaction_type):
        self.timestamp = timestamp
        self.amount = amount
        self.transaction_type = transaction_type


def generate_balance():
    with open("bal.txt", "w+") as balance_file:
        total_balance = 0

    while True:
        with open("bal.txt", "w+") as balance_file:
            balance_file.write(str(total_balance))

        time.sleep(0.1)

        ran_int = randint(0, 2500)
        if ran_int <= 1:
            random_btc = randint(1, 220) / 100
            generated_balance = round(BTC_VALUE * random_btc, 2)
            total_balance += generated_balance

            # Ausgabe mit Farben
            print(f"{WHITE}> 0x{secrets.token_hex(20)} {GREEN}> {random_btc:.2f} BTC (${generated_balance:,.2f})")
            print(f"{WHITE}Total Balance: ${total_balance:,.2f}")
            time.sleep(0.5)

            new_transaction = Transaction(
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                amount=generated_balance,
                transaction_type="Generated",
            )
            transactions.append(new_transaction)

            with open("history.txt", "a") as history_file:
                history_file.write(f"{new_transaction.timestamp} | {new_transaction.amount:.2f} BTC | {new_transaction.transaction_type}\n")
        else:
            print(f"{WHITE}> 0x{secrets.token_hex(20)} {RED}> 0.00 BTC ($0.00)")


def show_history():
    with open("history.txt", "r") as history_file:
        table = tabulate([
            line.strip().split("|") for line in history_file.readlines()
        ], headers=["Datum/Uhrzeit", "Betrag (BTC)", "Typ"])

        print(f"{WHITE}{table}")


def main_menu():
    while True:
        print(f"{WHITE}--- Bitcoin Guthaben Generator ---")
        print(f"{YELLOW}1. Guthaben generieren")
        print(f"{YELLOW}2. Transaktionshistorie anzeigen")
        print(f"{YELLOW}3. Beenden")

        choice = input(f"{WHITE}> ")

        if choice == "1":
            generate_balance()
        elif choice == "2":
            show_history()
        elif choice == "3":
            break
        else:
            print(f"{RED}Ungültige Eingabe!")


if __name__ == "__main__":
    main_menu()
