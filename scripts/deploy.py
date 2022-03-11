from brownie import accounts, Test, TestPayable, Caller


def main():
    print("Deploying Test...")
    t = Test.deploy({"from": accounts[0]})
    print(f"Test deplpyed at {t}...")

    print("Deploying Testpayable...")
    tp = TestPayable.deploy({"from": accounts[0]})
    print(f"TestPayable deplpyed at {tp}...")

    print("Deploying Caller...")
    c = Caller.deploy({"from": accounts[0]})
    print(f"Caller deplpyed at {c}...")

    print(f"Balances : a[0]={accounts[0].balance()}")
    print(f"TestPayable : {tp.balance()}")
    print(f"Caller : {c.balance()}")
    print("Funding the Caller contract with 5 ether...")
    accounts[0].transfer(c.address, amount="5 ether")
    print(f"Balances : a[0]={accounts[0].balance()}")
    print(f"TestPayable : {tp.balance()}")
    print(f"Caller : {c.balance()}")

    print("Calling callTest on Test...")
    tx = c.callTest(t, {"from": accounts[0]})
    tx.wait(1)

    print("Calling callTestPayable on TestPayable...")
    tx = c.callTestPayable(tp, {"from": accounts[0]})
    tx.wait(1)
    print("Called")
    print("Called")
    print(f"Balances : a[0]={accounts[0].balance()}")
    print(f"TestPayable : {tp.balance()}")
    print(f"Caller : {c.balance()}")

    print("Recuperating the ether...")
    tx = tp.withdraw({"from": accounts[0]})
    tx.wait(1)
    tx = c.withdraw({"from": accounts[0]})
    tx.wait(1)
    print("Called")
    print(f"Balances : a[0]={accounts[0].balance()}")
    print(f"TestPayable : {tp.balance()}")
    print(f"Caller : {c.balance()}")
