from tenis import Partida, NumeroDeJogadoresErrado


def teste_criar_partida():
    partida = Partida('Maria', 'João')
    assert type(partida) == Partida
    assert partida.jogadores == [
        {
            'nome': 'Maria',
            'pontos': 0,
            'vantagem': False,
            'games': 0,
            'sets': 0,
        },
        {
            'nome': 'João',
            'pontos': 0,
            'vantagem': False,
            'games': 0,
            'sets': 0,
        }
    ]

def test_adicionar_ponto():
    jog1 = 'Maria'
    jog2 = 'João'
    partida = Partida(jog1, jog2)

    partida.adicionar_ponto(0)
    assert partida.jogadores[0]['pontos'] == 15
    partida.adicionar_ponto(0)
    assert partida.jogadores[0]['pontos'] == 30
    partida.adicionar_ponto(0)
    assert partida.jogadores[0]['pontos'] == 40

def test_vantagem():
    jog1 = 'Maria'
    jog2 = 'João'
    partida = Partida(jog1, jog2)

    partida.adicionar_ponto(0)
    partida.adicionar_ponto(0)
    partida.adicionar_ponto(0)
    partida.adicionar_ponto(1)
    partida.adicionar_ponto(1)
    partida.adicionar_ponto(1)

    partida.adicionar_ponto(0)
    
    assert partida.vencedor == None
    assert partida.jogadores[0]['vantagem'] == True

def test_troca_vantagem():
    jog1 = 'Maria'
    jog2 = 'João'
    partida = Partida(jog1, jog2)

    partida.adicionar_ponto(0)
    partida.adicionar_ponto(0)
    partida.adicionar_ponto(0)
    partida.adicionar_ponto(1)
    partida.adicionar_ponto(1)
    partida.adicionar_ponto(1)

    partida.adicionar_ponto(0)

    partida.adicionar_ponto(1)
    assert partida.vencedor == None
    assert partida.jogadores[0]['vantagem'] == False
    assert partida.jogadores[1]['vantagem'] == False

    partida.adicionar_ponto(1)
    assert partida.vencedor == None
    assert partida.jogadores[0]['vantagem'] == False
    assert partida.jogadores[1]['vantagem'] == True


def test_vencer_game():
    jog1 = 'Maria'
    jog2 = 'João'
    partida = Partida(jog1, jog2)

    partida.adicionar_ponto(0)
    partida.adicionar_ponto(0)
    partida.adicionar_ponto(0)
    partida.adicionar_ponto(0)
    assert partida.jogadores[0]['games'] == 1


def teste_criar_partida_3_jogadores():
    try:
        Partida('Maria', 'Joao', 'Pedro')
        assert False
    except NumeroDeJogadoresErrado:
        assert True

def teste_criar_partida_1_jogadores():
    try:
        Partida('Maria')
        assert False
    except NumeroDeJogadoresErrado:
        assert True

def teste_criar_partida_0_jogadores():
    try:
        Partida()
        assert False
    except NumeroDeJogadoresErrado:
        assert True

def teste_empatado():
    jog1 = 'Maria'
    jog2 = 'João'
    partida = Partida(jog1, jog2)

    assert partida.situacao == Partida.EM_PROGRESSO
    partida.adicionar_ponto(0)
    partida.adicionar_ponto(0)
    partida.adicionar_ponto(0)
    partida.adicionar_ponto(1)
    partida.adicionar_ponto(1)
    partida.adicionar_ponto(1)
    assert partida.situacao == Partida.DEUCE
    partida.adicionar_ponto(1)
    assert partida.situacao == Partida.VANTAGEM
    partida.adicionar_ponto(1)
    assert partida.situacao == Partida.FINALIZADA
