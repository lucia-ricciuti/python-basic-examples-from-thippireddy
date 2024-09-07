id=1
firstName="Lucia"
lastName="Ricciuti"
ssn="123-45-6789"
hasInsurance=True
billingAmount="10000"
print(type(billingAmount))
billingAmount=float(billingAmount)
print(type(billingAmount))

print(f"""
    ID={id}, 
    First Name={firstName}, 
    Last Name={lastName}, 
    SSN={ssn[7:len(ssn)]},
    has insurance? {hasInsurance}
    Billing Amount={billingAmount}
    """)