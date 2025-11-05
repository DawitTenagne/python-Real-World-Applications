# ------------------------------------------------------------
# Program Name: account_balance.py
# Description:
#   This program reads transactions from a text file named
#   "accounts.txt" and updates the balances of three accounts:
#   a, b, and c. Each account starts with a balance of $500.
#   Deposits are represented by "<" and withdrawals by ">".
# ------------------------------------------------------------

# Step 1: Initialize the accounts with starting balances
a = 500
b = 500
c = 500

# Step 2: Open the file for reading
file = open("accounts.txt", "r")

# Step 3: Process each line in the file
for line in file:
    # Remove any extra whitespace (like newline characters)
    line = line.strip()

    # Split the line into parts: account, arrow, and amount
    parts = line.split(" ")
    account = parts[0]  # 'a', 'b', or 'c'
    arrow = parts[1]  # '<' for deposit, '>' for withdrawal
    amount = int(parts[2])  # convert amount from string to integer

    # Step 4: Update the correct account based on the arrow direction
    if account == "a":
        if arrow == "<":  # deposit
            a = a + amount
        elif arrow == ">":  # withdraw
            a = a - amount
    elif account == "b":
        if arrow == "<":
            b = b + amount
        elif arrow == ">":
            b = b - amount
    elif account == "c":
        if arrow == "<":
            c = c + amount
        elif arrow == ">":
            c = c - amount

# Step 5: Close the file after reading
file.close()

# Step 6: Print the final balances of all accounts
print("Final balance of account a:", a)
print("Final balance of account b:", b)
print("Final balance of account c:", c)