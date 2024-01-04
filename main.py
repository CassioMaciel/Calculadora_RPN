# noinspection PyPep8Naming
import Interface_Homem_Maquina as ihm
import operacoes as op


def main():
    stack = inicializa_stack()
    saida = 1
    while saida != 0:
        entrada = ihm.principal(stack)
        op.calculadora(entrada, stack)
        if entrada == 'q':
            saida = 0


def inicializa_stack():
    var_in = float(0)
    stack = [var_in]
    for i in range(9):
        stack.append(var_in)
    return stack


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
