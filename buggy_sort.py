def smaller_than(xs, pivot):
    return [x for x in xs if x < pivot]


def larger_than(xs, pivot):
    return [x for x in xs if x > pivot]


def sortk(x, xs):
    result = buggy_sort(smaller_than(xs, x))
    last_part = buggy_sort(larger_than(xs, x))
    result.append(x)
    result += last_part
    return result


def buggy_sort(list):
    if not list:
        return []
    else:
        return sortk(list[0], list[1:])
