rows = 10
print('(a)')
for i in range(rows):
    for j in range(0, i + 1):
        print("*", end=" ")  # print number
    print(" ")
print(" ")

print('(b)')
for i in range(rows , 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    print(" ")
print(" ")

 
print('(c)')
counter = 0
for i in range(rows , 0, -1):  
    for j in range(0, i):   
        print("*", end=" ")
    counter = counter + 2
    print("")            
    print(" "*counter , end="")    
print(" ")


print("(d)")
counter = (rows-1) *2
spacing =  counter
for i in range(rows):
    for j in range(0, i + 1):
        if counter == spacing:
            print(" "*(counter) , end="*")
        else:
            print("*", end=" ")  # print number
    counter = counter - 2
    print("")            
    print(" "*counter , end="")
    


                     
  





        