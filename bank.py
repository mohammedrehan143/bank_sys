import json
import os
from datetime import datetime

FILE_NAME = "data.json"


class Bank:

    def __init__(self):
        self.accounts = self.load_data()

    def load_data(self):

        if os.path.exists(FILE_NAME):

            with open(FILE_NAME, "r") as file:
                return json.load(file)

        return {}

    def save_data(self):

        with open(FILE_NAME, "w") as file:
            json.dump(self.accounts, file, indent=4)

    def create_account(self, username, pin):

        if username in self.accounts:
            return "Account already exists"

        self.accounts[username] = {
            "pin": pin,
            "balance": 0,
            "history": []
        }

        self.save_data()

        return "Account created successfully"

    def login(self, username, pin):

        if username in self.accounts:

            if self.accounts[username]["pin"] == pin:
                return True

        return False

    def deposit(self, username, amount):

        self.accounts[username]["balance"] += amount

        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        self.accounts[username]["history"].append(
            f"Deposited ₹{amount} on {time}"
        )

        self.save_data()

    def withdraw(self, username, amount):

        if self.accounts[username]["balance"] >= amount:

            self.accounts[username]["balance"] -= amount

            time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            self.accounts[username]["history"].append(
                f"Withdrawn ₹{amount} on {time}"
            )

            self.save_data()

            return True

        return False

    def get_balance(self, username):

        return self.accounts[username]["balance"]

    def get_history(self, username):

        return self.accounts[username]["history"]