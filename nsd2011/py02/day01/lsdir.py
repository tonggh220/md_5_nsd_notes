import os
import sys

def lsdir(mypath):
  for path, folders, files in os.walk(mypath):
      print(f'{path}:')
      for folder in folders:
          print(f'\033[34;1m{folder}\033[0m', end='\t')
      for file in files:
          print(file, end='\t')
      print('\n')

if __name__ == '__main__':
    lsdir(sys.argv[1])
