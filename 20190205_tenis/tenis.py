from copy import deepcopy

class NumeroDeJogadoresErrado(Exception):
    def __init__(self):
        pass

class Partida():
    EM_PROGRESSO = 0
    DEUCE = 1
    VANTAGEM = 2
    FINALIZADA = 3

    _jogadores = None
    _vencedor = None

    def __init__(self, *args):
        if len(args) != 2:
            raise NumeroDeJogadoresErrado()

        self._jogadores = [
            {
                'nome': nome,
                'pontos': 0,
                'vantagem': False,
                'games': 0,
                'sets': 0,
            }
            for nome in args
        ]

    @property
    def jogadores(self):
        return deepcopy(self._jogadores)

    @property
    def vencedor(self):
        return self._vencedor

    def _adicionar_game(self, indice_jodagor): 
        for j in self._jogadores:
            j['pontos'] = 0
            j['vantagem'] = False
        
        self._jogadores[indice_jodagor]['games'] += 1

    def adicionar_ponto(self, indice_jogador):
        indice_outro_jogador = 0 if indice_jogador == 1 else 1

        jogador = self._jogadores[indice_jogador]
        outro_jogador = self._jogadores[indice_outro_jogador]

        pontuacao_atual = jogador['pontos']
        pontuacao_atual_outro_jogador = outro_jogador['pontos']

        if self.situacao == self.DEUCE:
            jogador['vantagem'] = True
            outro_jogador['vantagem'] = False
            return

        if self.situacao == self.VANTAGEM:
            if jogador['vantagem']:
                self._vencedor = indice_jogador
                self._adicionar_game(indice_jogador)
            else:
                outro_jogador['vantagem'] = False
            return
        
        if pontuacao_atual == 40:
            self._vencedor = indice_jogador
            self._adicionar_game(indice_jogador)
            return

        jogador['pontos'] = (
            15 if pontuacao_atual == 0
            else 30 if pontuacao_atual == 15
            else 40
        )
    
    @property
    def situacao(self):
        if self._vencedor is not None:
            return self.FINALIZADA
        elif any(j['vantagem'] for j in self._jogadores):
            return self.VANTAGEM
        elif all(j['pontos'] == 40 for j in self.jogadores):
            return self.DEUCE
        else:
            return self.EM_PROGRESSO 
