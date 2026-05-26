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
            "history": [],
            "failed_attempts": 0,
            "blocked": False
        }

        self.save_data()

        return "Account created successfully"

    def login(self, username, pin):

        if username not in self.accounts:
            return False, "Invalid username or PIN"

        account = self.accounts[username]

        if account.get("blocked", False):
            return False, "Account is blocked. Please contact support."

        if account["pin"] == pin:
            account["failed_attempts"] = 0
            self.save_data()
            return True, "Login successful"

        account["failed_attempts"] = account.get("failed_attempts", 0) + 1

        if account["failed_attempts"] >= 3:
            account["blocked"] = True
            self.save_data()
            return False, "Invalid PIN. You have entered wrong PIN 3 times. Your account is blocked."

        self.save_data()
        remaining = 3 - account["failed_attempts"]
        return False, f"Invalid PIN. {remaining} chance(s) remaining."

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
