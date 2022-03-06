practis(1)

# Programming question 1
salary = int(input('Enter Salary :'))
if salary <= 1000:
    taxrate = 0
    tax = salary * 0 / 100
    netincome = salary - tax
    print("taxrate=", taxrate, "tax=", tax, "netincome=", netincome)
if salary > 1000:
    if salary <= 2500:
        taxrate = 10
        tax = salary * 10 / 100
        netincome = salary - tax
        print("taxrate=", taxrate, "tax=", tax, "netincome=", netincome)
if salary > 2500:
    if salary <= 4000:
        taxrate = 15
        tax = salary * 15 / 100
        netincome = salary - tax
        print("taxrate=", taxrate, "tax=", tax, "netincome=", netincome)
if salary > 4000:
    if salary <= 6000:
        taxrate = 20
        tax = salary * 20 / 100
        netincome = salary - tax
        print("taxrate=", taxrate, "tax=", tax, "netincome=", netincome)
if salary > 8000:
    taxrate = 30
    tax = salary * 30 / 100
    netincome = salary - tax
    print("taxrate=", taxrate, "tax=", tax, "netincome=", netincome)
    
    
    
    
    practis 2
    
    
    firstNum = int(input("enter first number :")
secondNum = int(input("enter second number :")
thirdNum = int(input("enter third number :")               
# first we should chack if this three sides can cake a triangle, then weshold if this triangle is right or not 
# for any triangle the sun of the lengths of any two sides is greater than the length of the third
# we can recognize right triangle by pythagorean theoren > pythagorean theoren : a^2 + b^2 - c^2 == 0
               
if firstNum + secondNum < thirdNum or firstNum + thirdNum < secondNum or secondNum + thirdnum < firstNum:
               print(" error : not a triangle")
else:
result1 = ((firstNum * 2) + (secondNum * 2)) - (thirdNum ** 2)
result2 = ((firstNum * 2) + (thirdNum * 2)) - (secondNum ** 2)              
result3 = ((thirdNum * 2) + (secondNum * 2)) - (firstNum ** 2)
if result1 == 0 or result2 == 0 or result3 == 0;
               print("right")
else:
               print("not right")
               
               
    practis-3
               
      input 1 = in(input("enter a number  : "))
  input 2 = in(input("enter a number  : "))
  input 3 = in(input("enter a number  : "))
  input 4 = in(input("enter a number  : "))
  input 5 = in(input("enter a number  : "))
  if input1 == input2 or input1 == input3 or input1 == input4 or input1 == input5:
  else input2 == input3 or input2 == input4 or input2 == input5 or input3 == input4 or input3 == input5 or input4 == input5:
  else:
   print("All unique"         
               
