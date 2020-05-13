import numpy as np


def find_kth(input_a, input_b, k):
    if len(input_a) == 0:
        return input_b[k - 1]
    if len(input_b) == 0:
        return input_a [k - 1]
    if k == 1:
        return min(input_a[0], input_b[0])

    tmp_a = 0
    tmp_b = 0
    index_a = int(k / 2) - 1
    index_b = index_a
    if index_a < len(input_a):
        tmp_a = input_a[index_a]
    else:
        tmp_a = input_a[-1]
        index_a = len(input_a) - 1
    if index_b < len(input_b):
        tmp_b = input_b[index_b]
    else:
        tmp_b = input_b[-1]
        index_b = len(input_b) - 1

    if tmp_a == tmp_b:
        if index_a == index_b and k % 2 == 0:
            return tmp_a
        else:
            return find_kth(input_a[index_a + 1:], input_b[index_b + 1:], k - index_a - index_b - 2)
    elif tmp_a < tmp_b:
        return find_kth(input_a[index_a + 1:], input_b, k - index_a - 1)
    else:
        return find_kth(input_a, input_b[index_b + 1:], k - index_b - 1)


for i in range(10000):
    test_a = sorted(np.random.randint(1, 50, size=100))
    test_b = sorted(np.random.randint(1, 50, size=100))
    k = np.random.randint(1, 200 + 1)
    test = sorted(np.append(test_a, test_b))
    if test[k - 1] != find_kth(test_a, test_b, k):
        print(test_a, test_b, k)
        print(test)
        print(test[k - 1])
        print(find_kth(test_a, test_b, k))
        print("++++++++++++++++++++++++++++++++++++++")

