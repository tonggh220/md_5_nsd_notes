import time

# n = 10000000
# start = time.time()
# result = n * (n + 1) / 2
# end = time.time()
# print(result, end - start)

result = 0

start = time.time()
for i in range(1, 10000001):
    result += i
end = time.time()

print(result, end - start)
