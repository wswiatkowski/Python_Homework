def foo(tab):
    """
    Function counts lowest absolute value of givens array's sections' sum.
    :param tab: Array given by user
    :return ret: Lowest possible absolute value of all sections' sum that could be found in given array.
    """
    ret = abs(sum(tab))

    for i in range(len(tab)):
        for j in range(i + 2, len(tab)):
            if abs(sum(tab[i:j])) < ret:
                ret = abs(sum(tab[i:j]))
    return ret
