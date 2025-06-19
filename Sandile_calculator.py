#This program is a simple scientific calculator 
# for students who need to perform 
# basic and advanced math operations like addition, 
# subtraction, multiplication, division, power, 
# square root, sine, cosine, tangent, and logarithm.
# The user can choose an operation by entering a number 
# from the options. The program keeps running in a loop 
# until the user enters option 5 to exit.

import math
while True:
  
  def addition():
     num1=int(input("enter your number    "))
     num2=int(input("enter your second number     "))
     total=num1+num2
     print("",total)
  def substraction():
      num1=int(input("enter your number    "))
      num2=int(input("enter your second number     "))
      total=num1-num2
      print("",total)
  def divition():
      num1=int(input("enter your number    "))
      num2=int(input("enter your second number     "))
      if num2!=0:
        total=num1/num2
        print("",total)
      else:
          print("invalid")
  def multiplication():
      num1=int(input("enter your number    "))
      num2=int(input("enter your second number     "))
      total=num1*num2
      print("",total)
  def power():
      num1=int(input("enter your number    "))
      num2=int(input("enter your second number     "))
      total=pow(num1,num2)
      print("",total)
  def square_root():
      num1=int(input("enter your number    "))
      total=math.sqrt(num1)
      print("",total)
  def sin():
      num1=int(input("enter your number    "))
      total=math.sin(num1)
      print("",total)
  def cos():
      num1=int(input("enter your number    "))
      total=math.cos(num1)
      print("",total)
  def tan():
      num1=int(input("enter your number    "))
      total=math.tan(num1)
      print("",total)
  def log():
      num1=int(input("enter your number    "))
      total=math.log(num1)
      print("",total)

      
      
      

  print("1. addition")
  print("2.substraction")
  print("3.division")
  print("4.multiplication")
  print("6. power")
  print("7.squre_root")
  print("8. sin")
  print("9.cos")
  print("10.tan")
  print("11.log")
  option=int(input("chose(1,2,3,4,6,7,8,9,10,11) or enter 5 to exit "))
  if option==1:
     addition()
  elif option==2:
      substraction()
  elif option==3:
       divition()
  elif option==4:
       multiplication()
  elif option==6:
      power()
  elif option==7:
      square_root()
  elif option==8:
      sin()
  elif option==9:
      cos()
  elif option==10:
      tan()
  elif option==11:
      log()
  elif option==5:
      print("goodbye have a good day")
      break
  else:
      print("invalid option try again")



    