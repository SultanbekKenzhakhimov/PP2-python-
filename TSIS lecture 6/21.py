import math
from time import sleep
def delay(f, m, *args):
  sleep(m / 1000)
  return f(*args) 
print(delay(lambda x: math.sqrt(x), 100, 16))
print(delay(lambda x: math.sqrt(x), 1000, 100))
print(delay(lambda x: math.sqrt(x), 2000, 25100))