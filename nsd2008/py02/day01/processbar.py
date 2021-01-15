import time
import sys

for i in range(10):
    time.sleep(0.2)
    print('#', end='')
    # 标准输出有缓冲区，将标准输出立即输出至屏幕
    sys.stdout.flush()
print()
