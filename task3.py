def foo(tab):
    """
    Function counts lowest absolute value of givens array's sections' sum.
    :param tab: Array given by user
    :return ret: Lowest possible absolute value of all sections' sum that could be found in given array.
    """
    temp_tab = [0]
    minimum = tab[0]

    for elem in tab:
        temp_tab.append(temp_tab[-1] + elem)

    temp_tab.sort()

    for i in range(1, len(temp_tab)):
        curr = temp_tab[i] - temp_tab[i - 1]

        if curr < minimum:
            minimum = curr

    return minimum
