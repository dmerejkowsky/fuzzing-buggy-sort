def smaller_than(xs, pivot):
    return [x for x in xs if x < pivot]


def larger_than(xs, pivot):
    return [x for x in xs if x > pivot]


def sortk(x, xs):
    result = sort(smaller_than(xs, x))
    last_part = sort(larger_than(xs, x))
    result.append(x)
    result += last_part
    return result


def sort(list):
    if not list:
        return []
    else:
        return sortk(list[0], list[1:])
