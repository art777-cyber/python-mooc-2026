a=float(input("Value of a: "))
b=float(input("Value of b: "))
c=float(input("Value of c: "))
from math import sqrt
print("")
print(f"The roots are {((0-b) + sqrt(b**2-(4*a*c)))/(2*a)} and {((0-b) - sqrt(b**2-(4*a*c)))/(2*a)}")