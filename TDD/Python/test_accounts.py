import pytest
from accounts import receive_money, add_transaction, send_money

# Helper: A fresh account for every test
def make_account():
    return{
        "account_number": "001",
        "balance": 100,
        "transactions": []
    }

# Test 1: Receiving money increases account balance
def test_receive_money_increase_balance():
    account = make_account()
    updated = receive_money(account, 50)
    assert updated["balance"] == 150

def test_receive_money_with_zero():
    account = make_account()   
    updated = receive_money(account, 0)
    assert updated["balance"] == 100

# Test 2: Adding a transaction updates history
def test_add_transaction_appears_in_history():
    account = make_account()
    updated = add_transaction(account, {"type": "credit", "amount": 50})
    assert len(updated["transactions"]) == 1

def test_add_multiple_transactions():
    account = make_account()
    add_transaction(account, {"type": "credit", "amount": 50})
    add_transaction(account, {"type": "credit", "amount": 30})
    assert len(account["transactions"]) == 2

# Test 3: Sending money reduces the balance
def test_send_money_reduces_balance():
    account = make_account()
    updated = send_money(account, 40)
    assert updated["balance"] == 60

def test_send_money_insufficient_funds_raises_error():
    account = make_account()
    with pytest.raises(ValueError):
        send_money(account, 999)        
