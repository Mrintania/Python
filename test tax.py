income = float(input("Input you income : "))
if income <= 150000:
    tax = 0
elif income <= 300000: 
    tax = (income - 150000) * 0.05
elif income <= 500000: 
    tax = (income - 300000) * 0.10 + 7500 
elif income <= 750000:
    tax = (income - 500000) * 0.15 + 27500 
elif income <= 1000000:
    tax = (income - 750000) * 0.20 + 65000 
elif income <= 2000000:
    tax = (income - 1000000) * 0.25 + 115000
elif income <= 4000000:
    tax = (income - 2000000) * 0.30 + 365000 
else:
    tax = (income - 1500000) * 0.35 + 1265000
print("You tax is : ", tax, "Bath!")