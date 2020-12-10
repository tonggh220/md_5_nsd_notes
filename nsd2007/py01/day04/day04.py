names = ['tom', 'jerry', 'bob', 'alice']

# >>> list(enumerate(names))
# [(0, 'tom'), (1, 'jerry'), (2, 'bob'), (3, 'alice')]

# for data in enumerate(names):
#     print(data)

# for data in enumerate(names):
#     print(data[0], data[1])

for i, name in enumerate(names):
    print(i, name)


# for i in [0, 1, 2, 3]:
#     print(i, names[i])

# for i in range(4):
#     print(i, names[i])

# for i in range(len(names)):
#     print(i, names[i])

# 0 tom
# 1 jerry
# 2 bob
# 3 alice
