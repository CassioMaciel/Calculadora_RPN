import subprocess
from pytest import mark

@mark.parametrize('arquivo',
                  [
                        ('.\\src\\main.py'),
                        ('.\\src\\operacoes.py'),
                        ('.\\src\\interface_homem_maquina.py'),
                  ])
def test_pylint(arquivo):
    result = subprocess.run(
        ['pylint', arquivo],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Verificar se a execução foi bem-sucedida
    assert result.returncode == 0, f'Pylint execution failed:\n{result.stderr}'

    # Verificar se a saída contém o resultado esperado
    assert 'Your code has been rated at 10.00/10' in result.stdout, \
        f'Unexpected Pylint rating:\n{result.stdout}'
