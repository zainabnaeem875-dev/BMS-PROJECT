import json
import random
import string
from pathlib import Path


class Bank:

    # ==========================================
    # DATABASE
    # ==========================================

    database = "data.json"

    def __init__(self):
        self.data = self.load_data()

    # ==========================================
    # LOAD DATA
    # ==========================================

    def load_data(self):

        if not Path(self.database).exists():
            return []

        try:
            with open(self.database, "r") as file:
                data = json.load(file)

                if isinstance(data, list):
                    return data

                return []

        except (json.JSONDecodeError, FileNotFoundError):
            return []

    # ==========================================
    # SAVE DATA
    # ==========================================

    def update(self):

        with open(self.database, "w") as file:
            json.dump(
                self.data,
                file,
                indent=4
            )

    # ==========================================
    # GENERATE ACCOUNT NUMBER
    # ==========================================

    def account_generate(self):

        while True:

            letters = random.choices(
                string.ascii_letters,
                k=3
            )

            numbers = random.choices(
                string.digits,
                k=3
            )

            special_character = random.choices(
                "!@#$%^&*",
                k=1
            )

            account_list = (
                letters
                + numbers
                + special_character
            )

            random.shuffle(account_list)

            account_number = "".join(account_list)

            # Make sure account number is unique
            if not any(
                user["accountNo"] == account_number
                for user in self.data
            ):
                return account_number

    # ==========================================
    # FIND USER
    # ==========================================

    def find_user(self, account_number, pin):

        account_number = str(account_number).strip()
        pin = str(pin).strip()

        for user in self.data:

            if (
                str(user.get("accountNo", "")) == account_number
                and str(user.get("pin", "")) == pin
            ):
                return user

        return None

    # ==========================================
    # CREATE ACCOUNT
    # ==========================================

    def create_account(
        self,
        name,
        age,
        email,
        pin
    ):

        # Clean input
        name = str(name).strip()
        email = str(email).strip()
        pin = str(pin).strip()

        # ------------------------------
        # Name validation
        # ------------------------------

        if not name:
            return False, "Please enter your name."

        # ------------------------------
        # Age validation
        # ------------------------------

        try:
            age = int(age)
        except (ValueError, TypeError):
            return False, "Age must be a number."

        if age < 18:
            return False, "You must be 18 years or older."

        # ------------------------------
        # Email validation
        # ------------------------------

        if not email:
            return False, "Please enter your email."

        if "@" not in email or "." not in email:
            return False, "Please enter a valid email address."

        # ------------------------------
        # PIN validation
        # ------------------------------

        if not pin:
            return False, "Please enter a PIN."

        if not pin.isdigit():
            return False, "PIN must contain numbers only."

        if len(pin) != 4:
            return False, "PIN must contain exactly 4 digits."

        # ------------------------------
        # Generate account number
        # ------------------------------

        account_number = self.account_generate()

        # ------------------------------
        # Create account
        # ------------------------------

        new_account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": account_number,
            "balance": 0
        }

        # Add account
        self.data.append(new_account)

        # Save data
        self.update()

        return True, new_account

    # ==========================================
    # DEPOSIT MONEY
    # ==========================================

    def deposit_money(
        self,
        account_number,
        pin,
        amount
    ):

        account_number = str(account_number).strip()
        pin = str(pin).strip()

        # Find account
        user = self.find_user(
            account_number,
            pin
        )

        if user is None:
            return False, "Account number or PIN is incorrect."

        # Amount validation
        try:
            amount = int(amount)
        except (ValueError, TypeError):
            return False, "Amount must be a number."

        if amount <= 0:
            return False, "Amount must be greater than 0."

        # Maximum deposit
        if amount > 10000:
            return False, "You can deposit maximum Rs. 10,000."

        # Deposit
        user["balance"] += amount

        # Save
        self.update()

        return True, user["balance"]

    # ==========================================
    # WITHDRAW MONEY
    # ==========================================

    def withdraw_money(
        self,
        account_number,
        pin,
        amount
    ):

        account_number = str(account_number).strip()
        pin = str(pin).strip()

        # Find account
        user = self.find_user(
            account_number,
            pin
        )

        if user is None:
            return False, "Account number or PIN is incorrect."

        # Amount validation
        try:
            amount = int(amount)
        except (ValueError, TypeError):
            return False, "Amount must be a number."

        if amount <= 0:
            return False, "Amount must be greater than 0."

        # Balance check
        if amount > user["balance"]:
            return False, "Insufficient balance."

        # Withdraw
        user["balance"] -= amount

        # Save
        self.update()

        return True, user["balance"]

    # ==========================================
    # ACCOUNT DETAILS
    # ==========================================

    def account_details(
        self,
        account_number,
        pin
    ):

        account_number = str(account_number).strip()
        pin = str(pin).strip()

        # Find account
        user = self.find_user(
            account_number,
            pin
        )

        if user is None:
            return False, "Account number or PIN is incorrect."

        return True, user

    # ==========================================
    # UPDATE ACCOUNT DETAILS
    # ==========================================

    def update_details(
        self,
        account_number,
        pin,
        name="",
        email="",
        new_pin=""
    ):

        account_number = str(account_number).strip()
        pin = str(pin).strip()

        # Find account
        user = self.find_user(
            account_number,
            pin
        )

        if user is None:
            return False, "Account number or PIN is incorrect."

        # --------------------------------
        # Update Name
        # --------------------------------

        if name.strip():

            user["name"] = name.strip()

        # --------------------------------
        # Update Email
        # --------------------------------

        if email.strip():

            email = email.strip()

            if "@" not in email or "." not in email:
                return False, "Please enter a valid email address."

            user["email"] = email

        # --------------------------------
        # Update PIN
        # --------------------------------

        if new_pin.strip():

            new_pin = new_pin.strip()

            if not new_pin.isdigit():
                return False, "New PIN must contain numbers only."

            if len(new_pin) != 4:
                return False, "New PIN must contain exactly 4 digits."

            user["pin"] = new_pin

        # Save changes
        self.update()

        return True, "Account details updated successfully."

    # ==========================================
    # DELETE ACCOUNT
    # ==========================================

    def delete_account(
        self,
        account_number,
        pin
    ):

        account_number = str(account_number).strip()
        pin = str(pin).strip()

        # Find account
        user = self.find_user(
            account_number,
            pin
        )

        if user is None:
            return False, "Account number or PIN is incorrect."

        # Delete account
        self.data.remove(user)

        # Save updated data
        self.update()

        return True, "Account deleted successfully."

    # ==========================================
    # TOTAL ACCOUNTS
    # ==========================================

    def total_accounts(self):

        return len(self.data)

    # ==========================================
    # TOTAL BALANCE
    # ==========================================

    def total_balance(self):

        return sum(
            user.get("balance", 0)
            for user in self.data
        )