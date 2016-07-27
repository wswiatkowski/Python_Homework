from itertools import combinations


def foo(tab):
    """
    Function counts number of subsets in given array;
    each subset has maximum element which is the sum of all the other elements of subset.
    :param tab: Array to find desired subsets in.
    :return ret: Number of desired subsets found in given array.
    """
    ret = 0

    for i in range(2, len(tab)):
        for comb in combinations(tab, i):
            print comb, sum(comb)
            if sum(comb) in tab:
                ret += 1

    return ret
