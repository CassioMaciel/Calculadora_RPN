import main
import Interface_Homem_Maquina
import operacoes as op
import clear
from pytest import mark



def test_adiciona_10_ao_stack():
    assert op.adiciona_ao_stack(10.0, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) == \
           [10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]



def test_adiciona_15_ao_stack():
    assert op.adiciona_ao_stack(15.0, [10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) == \
           [15.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]



def test_adiciona_20_ao_stack():
    assert op.adiciona_ao_stack(20.0, [15.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) == \
           [20.0, 15.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]



def test_adiciona_14_ao_stack():
    assert op.adiciona_ao_stack(14.0, [20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0]) == \
           [14.0, 20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0]



def test_soma_stack_1():
    assert op.soma_stack([20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0]) == \
        [35.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]



def test_soma_stack_2():
    assert op.soma_stack([8.72, 15.21, 3.45, 20.83, 7.11, 13.77, 9.04, 18.36, 14.5, 2.99]) == \
        [23.93, 3.45, 20.83, 7.11, 13.77, 9.04, 18.36, 14.5, 2.99, 0.0]



def test_subtrai_stack_1():
    assert op.subtrai_stack([2.45, 9.18, 13.76, 4.57, 15.93, 8.26, 10.09, 7.63, 14.28, 6.51]) == \
        [6.73, 13.76, 4.57, 15.93, 8.26, 10.09, 7.63, 14.28, 6.51, 0.0]



def test_subtrai_stack_2():
    assert op.subtrai_stack([16.88, 5.32, 12.74, 8.15, 3.09, 19.44, 11.27, 6.78, 9.02, 14.37]) == \
        [-11.56, 12.74, 8.15, 3.09, 19.44, 11.27, 6.78, 9.02, 14.37, 0.0]



def test_subtrai_stack_3():
    assert op.subtrai_stack([8.72, 15.21, 3.45, 20.83, 7.11, 13.77, 9.04, 18.36, 14.5, 2.99]) == \
        [6.49, 3.45, 20.83, 7.11, 13.77, 9.04, 18.36, 14.5, 2.99, 0.0]



def test_subtrai_stack_4():
    assert op.subtrai_stack([6.88, 14.26, 10.93, 3.75, 7.42, 12.19, 19.85, 5.11, 18.04, 11.55]) == \
        [7.38, 10.93, 3.75, 7.42, 12.19, 19.85, 5.11, 18.04, 11.55, 0.0]



def test_multiplica_stack_1():
    assert op.multiplica_stack([2.45, 9.18, 13.76, 4.57, 15.93, 8.26, 10.09, 7.63, 14.28, 6.51]) == \
        [22.491, 13.76, 4.57, 15.93, 8.26, 10.09, 7.63, 14.28, 6.51, 0.0]



def test_multiplica_stack_2():
    assert op.multiplica_stack([16.88, 5.32, 12.74, 8.15, 3.09, 19.44, 11.27, 6.78, 9.02, 14.37]) == \
        [89.8016, 12.74, 8.15, 3.09, 19.44, 11.27, 6.78, 9.02, 14.37, 0.0]



def test_multiplica_stack_3():
    assert op.multiplica_stack([8.72, 15.21, 3.45, 20.83, 7.11, 13.77, 9.04, 18.36, 14.5, 2.99]) == \
        [132.6312, 3.45, 20.83, 7.11, 13.77, 9.04, 18.36, 14.5, 2.99, 0.0]



def test_multiplica_stack_4():
    assert op.multiplica_stack([6.88, 14.26, 10.93, 3.75, 7.42, 12.19, 19.85, 5.11, 18.04, 11.55]) == \
        [98.1088, 10.93, 3.75, 7.42, 12.19, 19.85, 5.11, 18.04, 11.55, 0.0]



def test_divide_stack_1():
    assert op.divide_stack([2.45, 9.18, 13.76, 4.57, 15.93, 8.26, 10.09, 7.63, 14.28, 6.51]) == \
        [3.7469387755102037, 13.76, 4.57, 15.93, 8.26, 10.09, 7.63, 14.28, 6.51, 0.0]


def test_divide_stack_2():
    assert op.divide_stack([16.88, 5.32, 12.74, 8.15, 3.09, 19.44, 11.27, 6.78, 9.02, 14.37]) == \
        [0.3151658767772512, 12.74, 8.15, 3.09, 19.44, 11.27, 6.78, 9.02, 14.37, 0.0]


def test_divide_stack_3():
    assert op.divide_stack([8.72, 15.21, 3.45, 20.83, 7.11, 13.77, 9.04, 18.36, 14.5, 2.99]) == \
        [1.7442660550458715, 3.45, 20.83, 7.11, 13.77, 9.04, 18.36, 14.5, 2.99, 0.0]


def test_divide_stack_4():
    assert op.divide_stack([6.88, 14.26, 10.93, 3.75, 7.42, 12.19, 19.85, 5.11, 18.04, 11.55]) == \
        [2.072674418604651, 10.93, 3.75, 7.42, 12.19, 19.85, 5.11, 18.04, 11.55, 0.0]

def test_se_e_um_numero_recebe_3_e_retorna_que_é():
    assert op.e_numero("3") == True

def test_se_e_um_numero_recebe_207_e_retorna_que_é():
    assert op.e_numero("2.07") == True

def test_se_e_um_numero_recebe_207_e_retorna_que_é():
    assert op.e_numero("2.07") == True

def test_se_e_um_numero_recebe_joao_e_retorna_que_nao_e():
    assert op.e_numero("João") == False

def test_se_e_um_numero_recebe_joao_e_retorna_que_nao_e():
    assert op.e_numero("+") == False

@mark.skip('não vai rodar porque ainda não implementei')
def test_funcao_calculadora_soma_1():
    assert calculadora('+',[20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0]) == \
           [35.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]
