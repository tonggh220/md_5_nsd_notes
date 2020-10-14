# for j in range(1, 4):
#     print('hello')
########################
# for j in range(1, 4):
#     print('hello', end='\t')
# print()
########################
# for i in range(1, 4):
#     for j in range(1, 4):
#         print('hello', end='\t')
#     print()
########################
for i in range(1, 4):
    for j in range(1, i + 1):
        print('hello', end='\t')
    print()
