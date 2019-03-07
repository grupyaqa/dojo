from magnetismo import magnetizar
import types


def test_eh_funcao():
    assert isinstance(magnetizar, types.FunctionType)


def test_simples():
    pontos = []
    raio = 0
    cursor = (0, 0)
    assert magnetizar(pontos, raio, cursor) == (0, 0)


def test_magnetizando():
    pontos = [(51, 51)]
    raio = 5
    cursor = (51, 52)
    assert magnetizar(pontos, raio, cursor) == (51,51)


def test_sem_magnetizar():
    pontos = [(100, 100)]
    raio = 5
    cursor = (51, 52)
    assert magnetizar(pontos, raio, cursor) == (51,52)


def test_varios_magnetismos():
    pontos = [(1, 1), (4, 4)]
    raio = 5
    cursor = (2, 2)
    assert magnetizar(pontos, raio, cursor) == (1, 1)


def test_varios_magnetismos_nao_ordenados():
    pontos = [(4, 4), (1, 1)]
    raio = 5
    cursor = (2, 2)
    assert magnetizar(pontos, raio, cursor) == (1, 1)


def test_mesma_distancia():
    pontos = [(3, 3), (1, 1)]
    raio = 5
    cursor = (2, 2)
    assert magnetizar(pontos, raio, cursor) == (1, 1)


def test_magnetizando_euclidiana():
    pontos = [(2, 2), (1, 3)]
    raio = 5
    cursor = (0, 0)
    assert magnetizar(pontos, raio, cursor) == (2, 2)