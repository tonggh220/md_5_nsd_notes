from time import strftime

def full_backup():
    "用于完全备份"

def incr_backup():
    "用于增量备份"

if __name__ == '__main__':
    if strftime("%a") == "Mon":
        full_backup()
    else:
        incr_backup()
