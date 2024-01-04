# noinspection PyPep8Naming
import Interface_Homem_Maquina as ihm
import operacoes as op


def main():
    stack = op.inicializa_stack()
    saida = 1
    while saida != 0:
        entrada = ihm.principal(stack)
        stack = op.calculadora(entrada, stack)
        if entrada == 'q':
            saida = 0


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
