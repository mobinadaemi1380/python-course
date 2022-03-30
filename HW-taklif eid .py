#pracrtis 1


print('zavie mored nazar khod ra bar hasb darage vared konid')
daragee = float(input())
radian = (daragee * 3.14)/180
sinX = radian - ((radian**3) / (3*2*1)) + ((radian ** 5 )/(5*4*3*2*1)) - ((radian ** 7)/(7*6*5*4*3*2*1)) 

print(f'sinx = {sinX}')



#pracrtis 2

print('lotfan adad aval ra vared konid')
avali = int(input())

print('lotfan adad aval ra vared konid')
dovomi = int(input())

MagsoomMoshtarak=0

for r in range(2,avali+1) :
 if avali % r ==0 :
   for i in range(2,dovomi+1):
     if dovomi % i ==0 :
      if i==r:
        if i>= MagsoomMoshtarak:
          MagsoomMoshtarak = i
print(MagsoomMoshtarak)





#practis 3
adad = 0

while adad<=10000:
  ragam1 = adad%10
  ragam2 =(int(adad/10))%10
  ragam3 =(int(adad/100))%10
  ragam4 =(int(adad/1000))
  if 0<=adad<=9:
   if adad== (ragam1 )+(ragam2)+ (ragam3)+(ragam4) :
    print(adad)
  elif 10 <=adad<=99 :
   if adad== (ragam1**2 )+(ragam2**2)+ (ragam3**2)+(ragam4**2) :     
    print(adad)
  elif 100 <=adad<=999 :
   if adad== (ragam1**3 )+(ragam2**3)+ (ragam3**3)+(ragam4**3) :     
    print(adad)
  else :
   if adad== (ragam1**4 )+(ragam2**4)+ (ragam3**4)+(ragam4**4) :    
    print(adad) 
  adad += 1
adad += 1


#practis 4
def func(x): 
return x*3-x*2+2 
def derivFunc( x ):
 return 3 * x**2 - 2 * x def newtonRaphson(x): 
d = func(x) / derivFunc(x)
 for e in range(10): 
d = func(x) / derivFunc(x)  
x = x - d
 print("The number's root that you have entered is : ", "%.4f"% x) 
x0 = -20 
newtonRaphson( x0 )
 input()
  
  
  
  
  # practis 5
text = str(input("enter text: "))
s = int(input("enter shift: "))
result = ""
for i in range(len(text)):
    char = text[i]
    if char.isupper():
        result += chr((ord(char) + s - 65) % 26 + 65)
    else:
        result += chr((ord(char)
print("")
print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + result)
                       
                       
                       
#practic 6                       
sum_number = 0
average_number = 0
a = float(input("enter number: "))
minimum_number = 0
maximum_number = 0
for v in range(1, 19):
    a = float(input("enter number: "))
    sum_number += a
    if a > maximum_number:
        maximum_number = a

    elif a < minimum_number:
        minimum_number = a

print("sum: ", sum_number)
print("maximum: ", maximum_number)
print("minimum", minimum_number)
print("average: ", sum_number/20)                    
