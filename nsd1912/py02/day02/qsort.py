from random import randint

def qsort(seq):
    # 如果seq的长度小于2就返回它本身
    if len(seq) < 2:
        return seq

    # 假定第一个值是中间值，比它小的放到smaller中，大的放到larger中
    middle = seq[0]
    smaller = []
    larger = []

    for data in seq[1:]:
        if data <= middle:
            smaller.append(data)
        else:
            larger.append(data)

    return qsort(smaller) + [middle] + qsort(larger)


if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(qsort(nums))
