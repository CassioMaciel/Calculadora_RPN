import clear


def principal(stack):
    clear.clear()
    print("essa calculadora funciona através da notação RPN")
    print("caso queira fazer um teste, digite 5 <enter> 10 <enter> + <enter>")
    print("caso queira limpar, digit clc <enter>")
    print("caso queira sair, digite q <enter>", end="\n \n \n")
    for i in range(10)[::-1]:
        print(f"{i+1:2d}: {stack[i]}", end="\n")
    entrada = input('\n\n')
    return entrada
