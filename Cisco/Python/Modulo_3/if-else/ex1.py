# CÁLCULO DE IMPOSTO CONFORME REGRA DESCRITA NO REAME
income = float(input("Enter the annual income: "))

if income == 0:
    tax = 0
    tax = round(tax, 0)
    print("The tax is:", tax, "thalers")
elif income <= 85528:
    PIT = 0.18
    tax = (income * PIT)- 556.02
    tax = round(tax, 0)
    print("The tax is:", tax, "thalers")
elif income > 85528:
    PIT = 0.32
    tax = ((income-85528) * PIT) + 14939.02
    tax = round(tax, 0)
    print("The tax is:", tax, "thalers")
