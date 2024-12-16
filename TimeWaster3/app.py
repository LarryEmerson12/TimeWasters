import time

run = True
symbol = ['-', '\\', '|', '/']
sy = 0
b = 0
secs = 0
speed = 0.1

"""
Simple loading screen.
Adjust the speed at the speed
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
  time.sleep(speed)
  sy += 1
  b += 13
  secs = secs + speed
  """
  The output is below. If you want to edit it, do so.
  """
  if b > (5600):
    run = False
    for i in range(spaces):
      print()
    print(f'Added 56 packages, and audited 57 packages in {secs:.0f}s')
    print('Six packages are looking for funding')
    print('    run `npm fund` for details')
    print()
    print('3 low severity vulnerabilities')
    print()
    print('To adress all issues, run:')
    print('  npm audit fix')
    print()
    print('Run `npm audit` for details.')

"""
If you want some output after 'dependencies' are installed, then use the code in line 43.
"""