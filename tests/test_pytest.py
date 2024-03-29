import src as op


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


def test_se_e_um_numero_recebe_3_e_retorna_que_e():
    assert op.e_numero("3") is True


def test_se_e_um_numero_recebe_207_e_retorna_que_e():
    assert op.e_numero("2.07") is True


def test_se_e_um_numero_recebe_joao_e_retorna_que_nao_e():
    assert op.e_numero("João") is False


def test_se_e_um_numero_recebe_plus_e_retorna_que_nao_e():
    assert op.e_numero("+") is False


def test_calculadora_adiciona_10_ao_stack():
    assert op.calculadora(10.0, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) == \
           [10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


def test_calculadora_adiciona_15_ao_stack():
    assert op.calculadora(15.0, [10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) == \
           [15.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


def test_calculadora_adiciona_20_ao_stack():
    assert op.calculadora(20.0, [15.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) == \
           [20.0, 15.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


def test_calculadora_adiciona_14_ao_stack():
    assert op.calculadora(14.0, [20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0]) == \
           [14.0, 20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0]


def test_calculadora_soma_20_e_15():
    assert op.calculadora('+', [20.0, 15.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0]) == \
        [35.0, 10.0, 13.0, 27.5, 12.0, 16.0, 14.0, 13.0, 10.0, 0.0]


def test_calculadora_soma_8_e_15():
    assert op.calculadora('+', [8.72, 15.21, 3.45, 20.83, 7.11, 13.77, 9.04, 18.36, 14.5, 2.99]) == \
        [23.93, 3.45, 20.83, 7.11, 13.77, 9.04, 18.36, 14.5, 2.99, 0.0]


def test_calculadora_subtrai_2_de_9():
    assert op.calculadora('-', [2.45, 9.18, 13.76, 4.57, 15.93, 8.26, 10.09, 7.63, 14.28, 6.51]) == \
        [6.73, 13.76, 4.57, 15.93, 8.26, 10.09, 7.63, 14.28, 6.51, 0.0]


def test_calculadora_subtrai_stack_16_de_5():
    assert op.calculadora('-', [16.88, 5.32, 12.74, 8.15, 3.09, 19.44, 11.27, 6.78, 9.02, 14.37]) == \
        [-11.56, 12.74, 8.15, 3.09, 19.44, 11.27, 6.78, 9.02, 14.37, 0.0]


def test_calculadora_subtrai_8_de_15():
    assert op.calculadora('-', [8.72, 15.21, 3.45, 20.83, 7.11, 13.77, 9.04, 18.36, 14.5, 2.99]) == \
        [6.49, 3.45, 20.83, 7.11, 13.77, 9.04, 18.36, 14.5, 2.99, 0.0]


def test_calculadora_subtrai_6_de_14():
    assert op.calculadora('-', [6.88, 14.26, 10.93, 3.75, 7.42, 12.19, 19.85, 5.11, 18.04, 11.55]) == \
        [7.38, 10.93, 3.75, 7.42, 12.19, 19.85, 5.11, 18.04, 11.55, 0.0]


def test_calculadora_multiplica_2_e_9():
    assert op.calculadora('*', [2.45, 9.18, 13.76, 4.57, 15.93, 8.26, 10.09, 7.63, 14.28, 6.51]) == \
        [22.491, 13.76, 4.57, 15.93, 8.26, 10.09, 7.63, 14.28, 6.51, 0.0]


def test_calculadora_multiplica_16_e_5():
    assert op.calculadora('*', [16.88, 5.32, 12.74, 8.15, 3.09, 19.44, 11.27, 6.78, 9.02, 14.37]) == \
        [89.8016, 12.74, 8.15, 3.09, 19.44, 11.27, 6.78, 9.02, 14.37, 0.0]


def test_calculadora_multiplica_8_e_15():
    assert op.calculadora('*', [8.72, 15.21, 3.45, 20.83, 7.11, 13.77, 9.04, 18.36, 14.5, 2.99]) == \
        [132.6312, 3.45, 20.83, 7.11, 13.77, 9.04, 18.36, 14.5, 2.99, 0.0]


def test_calculadora_multiplica_6_e_14():
    assert op.calculadora('*', [6.88, 14.26, 10.93, 3.75, 7.42, 12.19, 19.85, 5.11, 18.04, 11.55]) == \
        [98.1088, 10.93, 3.75, 7.42, 12.19, 19.85, 5.11, 18.04, 11.55, 0.0]


def test_calculadora_divide_9_por_2():
    assert op.calculadora('/', [2.45, 9.18, 13.76, 4.57, 15.93, 8.26, 10.09, 7.63, 14.28, 6.51]) == \
        [3.7469387755102037, 13.76, 4.57, 15.93, 8.26, 10.09, 7.63, 14.28, 6.51, 0.0]


def test_calculadora_divide_5_por_16():
    assert op.calculadora('/', [16.88, 5.32, 12.74, 8.15, 3.09, 19.44, 11.27, 6.78, 9.02, 14.37]) == \
        [0.3151658767772512, 12.74, 8.15, 3.09, 19.44, 11.27, 6.78, 9.02, 14.37, 0.0]


def test_calculadora_divide_15_8():
    assert op.calculadora('/', [8.72, 15.21, 3.45, 20.83, 7.11, 13.77, 9.04, 18.36, 14.5, 2.99]) == \
        [1.7442660550458715, 3.45, 20.83, 7.11, 13.77, 9.04, 18.36, 14.5, 2.99, 0.0]


def test_calculadora_divide_14_por_6():
    assert op.calculadora('/', [6.88, 14.26, 10.93, 3.75, 7.42, 12.19, 19.85, 5.11, 18.04, 11.55]) == \
        [2.072674418604651, 10.93, 3.75, 7.42, 12.19, 19.85, 5.11, 18.04, 11.55, 0.0]


def test_calculadora_string_qualquer():
    assert op.calculadora('joao', [6.88, 14.26, 10.93, 3.75, 7.42, 12.19, 19.85, 5.11, 18.04, 11.55]) == \
        [6.88, 14.26, 10.93, 3.75, 7.42, 12.19, 19.85, 5.11, 18.04, 11.55]


def test_inicializa_stack():
    assert op.inicializa_stack() == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


def test_clear_stack():
    assert op.calculadora('clc', [6.88, 14.26, 10.93, 3.75, 7.42, 12.19, 19.85, 5.11, 18.04, 11.55]) == \
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
