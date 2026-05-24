from tkinter import *
from tkinter import messagebox
from bank import Bank

bank = Bank()

window = Tk()
window.title("Advanced Banking System")
window.geometry("700x600")
window.config(bg="#dfefff")

current_user = ""


# ================= MAIN FUNCTIONS =================

def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()


# ================= HOME PAGE =================

def home_page():

    clear_frame()

    title = Label(
        main_frame,
        text="BANKING SYSTEM",
        font=("Arial", 24, "bold"),
        bg="#dfefff",
        fg="darkblue"
    )

    title.pack(pady=40)

    Button(
        main_frame,
        text="LOGIN",
        width=20,
        height=2,
        font=("Arial", 14),
        bg="green",
        fg="white",
        command=login_page
    ).pack(pady=20)

    Button(
        main_frame,
        text="CREATE ACCOUNT",
        width=20,
        height=2,
        font=("Arial", 14),
        bg="blue",
        fg="white",
        command=create_account_page
    ).pack(pady=20)


# ================= CREATE ACCOUNT PAGE =================

def create_account_page():

    clear_frame()

    Label(
        main_frame,
        text="CREATE ACCOUNT",
        font=("Arial", 20, "bold"),
        bg="#dfefff"
    ).pack(pady=20)

    Label(main_frame, text="Username", bg="#dfefff").pack()

    entry_user = Entry(main_frame, width=30)
    entry_user.pack(pady=5)

    Label(main_frame, text="PIN", bg="#dfefff").pack()

    entry_pin = Entry(main_frame, show="*", width=30)
    entry_pin.pack(pady=5)

    def create():

        username = entry_user.get()
        pin = entry_pin.get()

        if username == "" or pin == "":
            messagebox.showerror("Error", "Fields cannot be empty")
            return

        result = bank.create_account(username, pin)

        messagebox.showinfo("Result", result)
        
        home_page()

    Button(
        main_frame,
        text="CREATE",
        width=15,
        bg="blue",
        fg="white",
        command=create
    ).pack(pady=20)

    Button(
        main_frame,
        text="BACK",
        width=15,
        command=home_page
    ).pack()


# ================= LOGIN PAGE =================

def login_page():

    clear_frame()

    Label(
        main_frame,
        text="LOGIN",
        font=("Arial", 20, "bold"),
        bg="#dfefff"
    ).pack(pady=20)

    Label(main_frame, text="Username", bg="#dfefff").pack()

    entry_user = Entry(main_frame, width=30)
    entry_user.pack(pady=5)

    Label(main_frame, text="PIN", bg="#dfefff").pack()

    entry_pin = Entry(main_frame, show="*", width=30)
    entry_pin.pack(pady=5)

    def login():

        global current_user

        username = entry_user.get()
        pin = entry_pin.get()

        if bank.login(username, pin):

            current_user = username

            messagebox.showinfo("Success", "Login Successful")

            dashboard()

        else:
            messagebox.showerror("Error", "Invalid Credentials")

    Button(
        main_frame,
        text="LOGIN",
        width=15,
        bg="green",
        fg="white",
        command=login
    ).pack(pady=20)

    Button(
        main_frame,
        text="BACK",
        width=15,
        command=home_page
    ).pack()


# ================= DASHBOARD =================

def dashboard():

    clear_frame()

    Label(
        main_frame,
        text=f"Welcome {current_user}",
        font=("Arial", 20, "bold"),
        bg="#dfefff",
        fg="darkblue"
    ).pack(pady=20)

    Button(
        main_frame,
        text="DEPOSIT",
        width=20,
        height=2,
        bg="green",
        fg="white",
        command=deposit_page
    ).pack(pady=10)

    Button(
        main_frame,
        text="WITHDRAW",
        width=20,
        height=2,
        bg="red",
        fg="white",
        command=withdraw_page
    ).pack(pady=10)

    Button(
        main_frame,
        text="BALANCE ENQUIRY",
        width=20,
        height=2,
        bg="orange",
        fg="white",
        command=show_balance
    ).pack(pady=10)

    Button(
        main_frame,
        text="MINI STATEMENT",
        width=20,
        height=2,
        bg="purple",
        fg="white",
        command=mini_statement
    ).pack(pady=10)

    Button(
        main_frame,
        text="LOGOUT",
        width=20,
        height=2,
        command=home_page
    ).pack(pady=10)


# ================= DEPOSIT PAGE =================

def deposit_page():

    clear_frame()

    Label(
        main_frame,
        text="DEPOSIT MONEY",
        font=("Arial", 20, "bold"),
        bg="#dfefff"
    ).pack(pady=20)

    Label(main_frame, text="Enter Amount", bg="#dfefff").pack()

    entry_amount = Entry(main_frame, width=30)
    entry_amount.pack(pady=10)

    def deposit():

        try:

            amount = float(entry_amount.get())

            if amount <= 0:
                messagebox.showerror("Error", "Invalid Amount")
                return

            bank.deposit(current_user, amount)

            messagebox.showinfo("Success", "Amount Deposited")

            dashboard()

        except ValueError:
            messagebox.showerror("Error", "Enter Valid Number")

    Button(
        main_frame,
        text="DEPOSIT",
        width=15,
        bg="green",
        fg="white",
        command=deposit
    ).pack(pady=20)

    Button(
        main_frame,
        text="BACK",
        width=15,
        command=dashboard
    ).pack()


# ================= WITHDRAW PAGE =================

def withdraw_page():

    clear_frame()

    Label(
        main_frame,
        text="WITHDRAW MONEY",
        font=("Arial", 20, "bold"),
        bg="#dfefff"
    ).pack(pady=20)

    Label(main_frame, text="Enter Amount", bg="#dfefff").pack()

    entry_amount = Entry(main_frame, width=30)
    entry_amount.pack(pady=10)

    def withdraw():

        try:

            amount = float(entry_amount.get())

            if amount <= 0:
                messagebox.showerror("Error", "Invalid Amount")
                return

            if bank.withdraw(current_user, amount):

                messagebox.showinfo("Success", "Amount Withdrawn")

                dashboard()

            else:
                messagebox.showerror("Error", "Insufficient Balance")

        except ValueError:
            messagebox.showerror("Error", "Enter Valid Number")

    Button(
        main_frame,
        text="WITHDRAW",
        width=15,
        bg="red",
        fg="white",
        command=withdraw
    ).pack(pady=20)

    Button(
        main_frame,
        text="BACK",
        width=15,
        command=dashboard
    ).pack()


# ================= BALANCE =================

def show_balance():

    balance = bank.get_balance(current_user)

    messagebox.showinfo(
        "Balance",
        f"Current Balance: ₹{balance}"
    )


# ================= MINI STATEMENT =================

def mini_statement():

    clear_frame()

    Label(
        main_frame,
        text="MINI STATEMENT",
        font=("Arial", 20, "bold"),
        bg="#dfefff"
    ).pack(pady=20)

    history = bank.get_history(current_user)

    text_box = Text(main_frame, width=60, height=15)
    text_box.pack(pady=10)

    if len(history) == 0:

        text_box.insert(END, "No Transactions Found")

    else:

        for item in history:
            text_box.insert(END, item + "\n")

    Button(
        main_frame,
        text="BACK",
        width=15,
        command=dashboard
    ).pack(pady=10)


# ================= MAIN FRAME =================

main_frame = Frame(window, bg="#dfefff")
main_frame.pack(fill="both", expand=True)

home_page()

window.mainloop()