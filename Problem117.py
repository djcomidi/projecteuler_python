from EulerTools import Memoize


@Memoize
def fill_count(size):
    ways = 1
    for w in [2, 3, 4]:
        for pos in range(size - w + 1):
            ways += fill_count(size - (pos + w))
    return ways


result = fill_count(50)
print(result)
