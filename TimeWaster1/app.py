import time

run = True

i = 10
while run:
  print(i)
  time.sleep(0.001)
  i = i * 10

"""
Repeats until you get this error:
Increase the time.sleep() to get slower results.
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
"""