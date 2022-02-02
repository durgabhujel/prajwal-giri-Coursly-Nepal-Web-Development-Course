from calculator import *
from calculator import add, subtract
import calculator as c

a = 54
b = 9

# s
# r = add(a,b)
# r2 = subtract(a,b)

r = c.add(a,b)
r2 = c.subtract(a,b)
print(f"The result of adding {a} and {b} is {r}")
print(f"The result of subtracting {a} and {b} is {r2}")