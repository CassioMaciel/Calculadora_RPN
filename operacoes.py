"""
Módulo de Funções Matemáticas

Este módulo contém diversas funções para realizar as operações matemáticas
necessárias a calculadora.

Funções Disponíveis:
---------------------

1. adiciona_ao_stack(entrada, stack): Adiciona um número ao stack

   Exemplo:
    >>> adiciona_ao_stack \
    (10.0, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    [10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

2. `soma_stack(stack)`: Soma os 2 primeiros valores do stack.

   Exemplo:
    >>> soma_stack \
    ([20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [35.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]

3. `subtrai_stack(stack)`: Retorna o segundo número do stack menos o primeiro.

   Exemplo:
    >>> subtrai_stack( \
    [20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [-5.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]

4. `multiplica_stack(stack)`: Retorna o produto dos números a e b.

   Exemplo:
    >>> multiplica_stack(\
    [20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [300.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]

5. `divide_stack(stack)`: Retorna o resultado da divisão de a por b.

   Exemplo:
    >>> divide_stack(\
    [20.0, 50.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [2.5, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]

5. `e_numero(entrada)`: Retorna se a entrada é ou não um numero.

   Exemplo:
    >>> e_numero("3.5")
    True
    >>> e_numero("F3d4.3")
    False

6. `inicializa_stack()`: Faz um stack novo com 10 valores 0.0.

   Exemplo:
   >>> inicializa_stack()
   [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

7. `calculadora(entrada, stack)`: É a função que escolhe as outras funções.

   Exemplo:
    >>> calculadora(10.0, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    [10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    >>> calculadora \
    ('+',[20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [35.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]

    >>> calculadora \
    ('-',[20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [-5.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]

    >>> calculadora \
    ('*',[20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [300.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]

    >>> calculadora \
    ('/',[20.0, 50.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [2.5, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]
"""


def adiciona_ao_stack(entrada, stack):
    """
    :param entrada: float
    :param stack:
    :return:
    >>> adiciona_ao_stack \
    (10.0, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    [10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    >>> adiciona_ao_stack \
    (15.0, [10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    [15.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    >>> adiciona_ao_stack \
    (20.0, [15.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    [20.0, 15.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    >>> adiciona_ao_stack \
    (14.0, [20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
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
    >>> soma_stack(\
    [20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
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
    >>> subtrai_stack( \
    [20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
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
    >>> multiplica_stack( \
    [20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
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
    >>> divide_stack( \
    [20.0, 50.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
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


def inicializa_stack():
    """
        Inicializa uma stack com 10 elementos iguais a 0.

        Essa função cria uma lista (stack) com 10 elementos,
        cada um inicializado com o valor 0.

        Returns:
        --------
        list:
            Uma lista com 10 elementos, todos iguais a 0.

        Exemplo:
        --------
        >>> inicializa_stack()
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        """
    var_in = float(0)
    stack = [var_in]
    for _ in range(9):
        stack.append(var_in)
    return stack


def calculadora(entrada, stack):
    """
        Realiza operações básicas de soma, subtração, multiplicação e divisão.

        Esta função aceita uma operação uma string digitada pelo usuario e o
        stack.
        Caso a sitring seja um número, será adicionado ao stack.
        Caso seja uma operação, será feita com o stack fornecido


        Parâmetros:
        -----------
        entrada : str

        stack : list
            Uma lista com 10 números.

        Returns:
        --------
        list
            O stack resultante

        Exemplo:
        --------
    >>> calculadora(10.0, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    [10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    >>> calculadora \
    ('+',[20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [35.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]

    >>> calculadora \
    ('-',[20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [-5.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]

    >>> calculadora \
    ('*',[20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [300.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]

    >>> calculadora \
    ('/',[20.0, 50.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [2.5, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]

    >>> calculadora \
    ('clc',[20.0, 50.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0])
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    """

    if e_numero(entrada):
        stack = adiciona_ao_stack(float(entrada), stack)
    elif entrada == '+':
        stack = soma_stack(stack)
    elif entrada == '-':
        stack = subtrai_stack(stack)
    elif entrada == '/':
        stack = divide_stack(stack)
    elif entrada == '*':
        stack = multiplica_stack(stack)
    elif entrada == 'clc':
        stack = inicializa_stack()
    return stack


if __name__ == '__main__':
    import doctest
    doctest.testmod()
