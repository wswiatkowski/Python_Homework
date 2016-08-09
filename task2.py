def foo(tab):
    """
    Function returns the greatest subarray length in given array which begins and ends with the same int.
    :param tab: Array in which we look for longest subarray
    :return: Maximum subarray length
    """

    duplicates = [x for x in tab if tab.count(x) > 1]
    idxs = []

    for dupl in duplicates:
        idxs.append(tab.index(dupl))
        tab[idxs[-1]] = None

    tup = zip(duplicates, idxs)
    tup.sort()

    max_len = 0
    curr = 0
    for count in [duplicates.count(x) - 1 for x in set(duplicates)]:
        max_len = max(max_len, abs(tup[curr][1] - tup[curr + count][1]))
        curr += count

    return max_len
