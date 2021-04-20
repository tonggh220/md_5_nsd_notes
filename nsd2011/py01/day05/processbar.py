import time
import sys

for i in range(1, 21):
    # print(f'\r{"#" * i}', end='')
    print('#', end='')
    sys.stdout.flush()  # 立即输出
    time.sleep(0.3)
print()
