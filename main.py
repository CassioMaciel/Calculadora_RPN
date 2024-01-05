"""
Esse módulo é o responsável por rodar o programa Calculadora RPN
"""
# noinspection PyPep8Naming
import interface_homem_maquina as ihm
import operacoes as op


def main() -> None:
    """
    Função principal do programa.

    Responsabilidades:
    - Inicializa a stack.

    - Chama a função principal de interação com o usuário para obter uma
    entrada.

    - Chama a calculadora com a entrada fornecida e a stack atual.

    - Continua a execução enquanto o usuário desejar.

    - Encerra a execução se o usuário inserir 'q'.

    Parâmetros:
    -----------
    Nenhum.

    Returns:
    --------
    None
        Esta função não retorna nenhum valor.

    Exemplo:
    --------
    >>> main()
    Execução principal concluída.
    """
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
