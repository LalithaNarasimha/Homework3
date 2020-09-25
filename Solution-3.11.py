Gallons = 0
Miles = 0
Total_miles = 0
Total_gallons = 0
Average = 0
num = 1
Mileage = 0

record_number = int(input('Enter the number of records maintained to calculate miles per gallon '))

while(num <= record_number):
    Gallons = float(input("Enter the Gallons used "))
    Miles = int(input("Enter the miles driven "))
    Mileage = Miles/Gallons
    print(f'The miles/gallon for this tank was {Mileage:.6f}')
    num = num + 1
    Total_miles = Total_miles + Miles
    Total_gallons = Total_gallons + Gallons

Average = Total_miles/Total_gallons
print(f'The overall average miles/gallon was {Average:.6f}') 
