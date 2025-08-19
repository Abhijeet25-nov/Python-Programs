def simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> list[str]:
    res=[]
    i=0
    while i < len(withdrawals):
        amount=withdrawals[i]
        if amount<=balance:
            balance -= amount
            res.append(f"Withdrwan: {amount}")
        else:
            res.append(f"Insufficient funds for requested amount: {amount}")
        i=i+1 
    res.append(f"Remaining Balance: {balance}")
    return res