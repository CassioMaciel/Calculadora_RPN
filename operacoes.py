def adiciona_ao_stack(entrada, stack):
    """
    :param entrada: float
    :param stack:
    :return:
    >>> adiciona_ao_stack(10.0, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    [10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    >>> adiciona_ao_stack(15.0, [10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    [15.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    >>> adiciona_ao_stack(20.0, [15.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    [20.0, 15.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    >>> adiciona_ao_stack(14.0, [20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [14.0, 20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0]
    """
    for i in range(9):
        # noinspection PyTypeChecker
        posicao = 9-i
        stack[posicao] = stack[posicao-1]
    stack[0] = entrada
    return stack


def soma_stack(stack):
    """

    :param stack:
    :return:
    >>> soma_stack([20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [35.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]
    """
    stack[0] = stack[0] + stack[1]
    for i in range(1, 9):
        stack[i] = stack[i+1]
    stack[9] = 0.0
    return stack


def subtrai_stack(stack):
    """

    :param stack:
    :return:
    >>> subtrai_stack([20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [-5.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]
    """
    stack[0] = round(stack[1] - stack[0], 14)
    for i in range(1, 9):
        stack[i] = stack[i+1]
    stack[9] = 0.0
    return stack


def multiplica_stack(stack):
    """

    :param stack:
    :return:
    >>> multiplica_stack([20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [300.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]
    """
    stack[0] = stack[0] * stack[1]
    for i in range(1, 9):
        stack[i] = stack[i+1]
    stack[9] = 0.0
    return stack


def divide_stack(stack):
    """
    :param stack:
    :return:
    >>> divide_stack([20.0, 50.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [2.5, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]
    """

    stack[0] = stack[1] / stack[0]
    for i in range(1, 9):
        stack[i] = stack[i+1]
    stack[9] = 0.0
    return stack


def e_numero(entrada: str):
    """:return:
    >>> e_numero("3")
    True
    >>> e_numero("3.5")
    True
    >>> e_numero("F3d4.3")
    False"""
    # noinspection PyTypeChecker
    boleano = True
    try:
        float(entrada)
    except ValueError:
        # noinspection PyTypeChecker
        boleano = False

    return boleano


if __name__ == '__main__':
    import doctest
    doctest.testmod()
