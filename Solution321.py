amount = float(input("Enter the amount "))
print("Your change is :")
print(f'{int(amount//25)} quarters')
amount = amount %25

print(f'{int(amount//10)} dimes')
amount = amount %10

print(f'{int(amount//5)} nickels')
amount = amount %5

print(f'{int(amount//1)} pennies')






