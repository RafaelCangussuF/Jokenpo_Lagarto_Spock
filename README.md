# Jokenpo_Lagarto_Spock

## Introdução
Criação de um jogo de Pedra, Papel, Tesoura, Lagarto e Spock com servidor em Python e cliente em Java, ambos jogando.

O Cliente em Java inicia a conexão com o servidor em Python e recebe comandos do usuário para escolher o palpite a ser enviado, o servidor recebe esse resultado, decide seu próprio palpite e define quem venceu ou perdeu a rodada.

O servidor então manda uma mensagem ao cliente com os palpites de cada um e o vencedor da rodada, o servidor calcula a pontuação acumulada e quando terminam as 15 rodadas ele define o vencedor do jogo.

Ambas as escolhas de palpites podem ser aleatórias, porém o usuário pode definir qual palpite ele deseja enviar para o servidor, enquanto o servidor é sempre aleatório.

Os códigos estão comentados de forma a facilitar o seu entendimento.
