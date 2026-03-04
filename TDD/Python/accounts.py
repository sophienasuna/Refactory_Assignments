def receive_money(account, amount):
    # Function 1: Add incoming money to account balance
    account["balance"]+= amount
    return account

def add_transaction(account, transaction):
    # Function 2:Add a transaction to history
    account["transactions"].append(transaction)
    return account

def send_money(account, amount):
    # Function 3: Deduct outgoing money from account balance
    if amount > account["balance"]:
        raise ValueError("Insufficient funds")
    account["balance"] -= amount
    return account
    