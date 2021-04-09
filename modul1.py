import datetime  #1
now = datetime.datetime.now()
print ("Текущая дата и время: ", now.strftime("%Y-%m-%d %H:%M:%S"))

import datetime  #2
now = datetime.datetime.now()

name = input("как вас зовут?")
age = int (input ("Cколько вам лет?"))
year = str((now.year - age) + 100)
print(name + ", Baм будет 100 лет в"  + year + " году")

def fibonacci(n):  #3
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
 
print(fibonacci(10))


import math  #4

