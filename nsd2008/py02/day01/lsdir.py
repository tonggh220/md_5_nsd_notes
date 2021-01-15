import os

for path, folders, files in os.walk('/tmp/mydemo'):
    print("%s:" % path)
    for folder in folders:
        print('\033[34;1m%s\033[0m' % folder, end='\t')
    for file in files:
        print(file, end='\t')
    print('\n')
