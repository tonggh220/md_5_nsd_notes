import os
import sys

def lsdir(dest):
    for path, folders, files in os.walk(dest):
        print('%s:' % path)
        for folder in folders:
            print('\033[34;1m%s\033[0m' % folder, end='\t')
        for file in files:
            print(file, end='\t')
        print('\n')

if __name__ == '__main__':
    lsdir(sys.argv[1])
