import time

"""
Loading screen.
Adjust the speed.
"""
run = True
h = 0
t = 100
spaces = 0

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
    for i in range(spaces):
        print()
    print('[',end="")
    print('#' * h, end="")
    print('-' * (t - h),end="")
    print(']')
    time.sleep(0.1)
    h = h + 1
    if h > 99:
        run = False
        for i in range(spaces):
            print()
        print('Loading Complete.')
        time.sleep(1)
        for i in range(spaces):
            print()
        print('Welcome to the Lobby.')
        # Do whatever you want here.