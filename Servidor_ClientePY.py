# Bibliotecas
import socket
import random

# Identificação do HOST E PORT do servidor
HOST = 'localhost'  # Identifica o nome do servidor
PORT = 40001  # Identifica a porta do servidor
addr = (HOST, PORT)

# Lista com as possíveis jogadas que podem ser escolhidas pelo servidor.
opcoesJogadas = ['Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock']

# O mecanismo de Socket foi criado para receber a con1exão, onde na função passamos 2 argumentos, AF_INET que declara a família do protocolo;
# Se fosse um envio via Bluetooth por exemplo, seria: AF_BLUETOOTH, e o SOCKET_STREAM, indica que será TCP/IP.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM identificação do TCP
# A constante AF_INET faz parte de um grupo denominado famílias de endereços, ou address families, que constitui exatamente o primeiro parâmetro opcional do construtor socket.
# A AF_INET abrange os endereços do tipo IPv4, antigo padrão da Internet.

# Esta linha define para qual IP e porta o servidor deve aguardar a conexão.
sock.bind(addr)

# Define o limite de conexões. E no caso, estamos limitando em 5 conexões.
sock.listen(5)

print("Aguardando conexão de um cliente:")

conn, ender = sock.accept()  # Conexão e endereço

print('Connectado com',
      ender)  # Apresentação do endereço do cliente, composto de nome do host e a porta que foram conectados.
print("\nOs palpites do servidor são ALEATÓRIOS!\n")

ClientePy = 0
ClienteJava = 0
rodada = 0
while True:
    # O servidor fica liberado por tempo indeterminado ou até a conexão ser encerrada.
    # Aguarda um dado enviado pela rede de até 1024 Bytes, a função ‘recv’ possui somente 1 argumento que é o tamanho do Buffer.
    data = conn.recv(1024)  # 1024 Byter serão recebidos do client


    # print("Resposta do cliente:", data.decode())

    if not data:  # Quando não tiver mais nada dentro do data a conexão é encerrada
        print("\nConexão encerrada!\n")

        conn.close()  # Serve para fechar a conexão entre as aplicações.
        break

    palpiteClient = str(
        data.decode())  # Utilizado para decodificar e transformar a mensagem em string enviada pelo cliente.
    palpiteServ = random.choice(
        opcoesJogadas)  # O palpite do servidor é escolhido de forma randômica, as opções estão dentro da lista opcoesJogadas.

    print("* O Servidor respondeu:", palpiteServ)  # Apresenta o palpite do servidor
    print(palpiteClient)

    # Verifica quando o cliente ganha a jogada
    if ((palpiteClient == 'Tesoura' and palpiteServ == 'Papel') or (
            palpiteClient == 'Tesoura' and palpiteServ == 'Lagarto') or (
            palpiteClient == 'Papel' and palpiteServ == 'Pedra') or (
            palpiteClient == 'Papel' and palpiteServ == 'Spock') or (
            palpiteClient == 'Pedra' and palpiteServ == 'Tesoura') or (
            palpiteClient == 'Pedra' and palpiteServ == 'Lagarto') or (
            palpiteClient == 'Lagarto' and palpiteServ == 'Papel') or (
            palpiteClient == 'Lagarto' and palpiteServ == 'Spock') or (
            palpiteClient == 'Spock' and palpiteServ == 'Tesoura') or (
            palpiteClient == 'Spock' and palpiteServ == 'Pedra')
    ):
        ganhador = 'Cliente'
        ClienteJava = ClienteJava + 1
        rodada = rodada + 1

    # Verifica quando o Servidor ganha a jogada
    if ((palpiteServ == 'Tesoura' and palpiteClient == 'Papel') or (
            palpiteServ == 'Tesoura' and palpiteClient == 'Lagarto') or (
            palpiteServ == 'Papel' and palpiteClient == 'Pedra') or (
            palpiteServ == 'Papel' and palpiteClient == 'Spock') or (
            palpiteServ == 'Pedra' and palpiteClient == 'Tesoura') or (
            palpiteServ == 'Pedra' and palpiteClient == 'Lagarto') or (
            palpiteServ == 'Lagarto' and palpiteClient == 'Papel') or (
            palpiteServ == 'Lagarto' and palpiteClient == 'Spock') or (
            palpiteServ == 'Spock' and palpiteClient == 'Tesoura') or (
            palpiteServ == 'Spock' and palpiteClient == 'Pedra')):
        ganhador = 'Servidor'
        ClientePy = ClientePy + 1
        rodada = rodada + 1

    # Verificação em caso de empate
    if (palpiteClient == palpiteServ):
        ganhador = 'Empate'
        rodada = rodada + 1

    # String de retorno para o cliente
    result = '- Cliente Java: ' + str(palpiteClient) + '\n- Servidor / Cliente Py: ' + str(palpiteServ) + '\n=> Ganhador da Rodada: ' + str(
        ganhador) + '\n' # Concatenação dos resultados, sendo eles apresentados para o cliente

    # Utilizado para enviar o resultodo para o cliente.
    print(result)
    print(f'ClientePy Pontuacao = {ClientePy}')
    print(f'ClienteJava Pontuacao = {ClienteJava}')
    if(ClienteJava > ClientePy and rodada ==15):
        print('Cliente Java Vencedor')
    if(ClientePy > ClienteJava and rodada==15):
        print('Cliente Py Vencedor')
    if(ClientePy == ClienteJava and rodada==15):
        print('Empate')
    conn.sendall(bytes(str(result), 'utf8'))
