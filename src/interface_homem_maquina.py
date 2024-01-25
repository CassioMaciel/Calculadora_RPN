"""
Módulo interface_homem_maquina

Este módulo contém funções relacionadas à interação com o usuário,
incluindo impressões, importações e qualquer outra interação com o
homem (usuário).

Funções Disponíveis:
---------------------

1. `principal(stack)`: A tela principal da calculadora.

2. `clear()`: limpa a tela.

"""

from os import system, name


def principal(stack) -> str:
    """
    Essa função é a tela principal da calculadora, onde imprime o stack e pega
    a entrada do usuário
    :param stack: list
    :return: str
    """
    clear()
    print("essa calculadora funciona através da notação RPN")
    print("caso queira fazer um teste, digite 5 <enter> 10 <enter> + <enter>")
    print("caso queira limpar, digit clc <enter>")
    print("caso queira sair, digite q <enter>", end="\n \n \n")
    for i in range(10)[::-1]:
        print(f"{i+1:2d}: {stack[i]}", end="\n")
    entrada = input('\n\n')
    return entrada


def clear() -> None:
    """
     Essa função limpa a tela do usuário, independente so sistema operacional
     """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
