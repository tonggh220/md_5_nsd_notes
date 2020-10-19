import os
import sys

def lsdir(path):
    for p, folders, files in os.walk(path):
        print('%s:' % p)
        for folder in folders:
            print('\033[34;1m%s\033[0m' % folder, end='\t')
        for file in files:
            print(file, end='\t')
        print('\n')


if __name__ == '__main__':
    lsdir(sys.argv[1])

