import time

running = True
i = 1

while running:
  if i > 130:
    i = 1
  print('0' * i)
  time.sleep(0.01)
  i = i + 1

"""
Adjust the speed.
"""