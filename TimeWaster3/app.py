import time

run = True
symbol = ['-', '\\', '|', '/']
sy = 0
b = 0

"""
Simple loading screen.
Adjust the speed at the time.sleep(0.1)
You can make it faster, slower, or normal.
To make it more normal, adjust the difference for the bytes at 'b += 2'.
"""

vscode = input('VSCode? (y/n)').lower()

if vscode == 'y':
  f = input('Fullscreen? (y/n)').lower()
  if f == 'y':
    spaces = 34
  else:
    spaces = 9
else:
  spaces = int(input('How high is your terminal? (lines)'))
  spaces = spaces - 1

while run:
  if sy > 3:
    sy = 0
  for i in range(spaces):
    print()
  print(symbol[sy], end="")
  print(f' Installing Dependecies{'.' * sy}{' ' * (4 - sy)}[{b}MB]')
  time.sleep(0.1)
  sy += 1
  b += 13