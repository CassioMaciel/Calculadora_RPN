# noinspection PyPep8Naming
import Interface_Homem_Maquina as ihm
import operacoes as op


def main():
    stack = inicializa_stack()
    saida = 1
    while saida != 0:
        entrada = ihm.principal(stack)
        if op.e_numero(entrada):
            stack = op.adiciona_ao_stack(float(entrada), stack)
        elif entrada == '+':
            stack = op.soma_stack(stack)
        elif entrada == '-':
            stack = op.subtrai_stack(stack)
        elif entrada == '/':
            stack = op.divide_stack(stack)
        elif entrada == '*':
            stack = op.multiplica_stack(stack)
        elif entrada == 'clc':
            stack = inicializa_stack()
        elif entrada == 'q':
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
