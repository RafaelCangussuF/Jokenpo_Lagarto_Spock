package org.example;

import java.io.*;
import java.net.Socket;
import java.util.Random;
import java.util.Scanner;



public class Main {
    static String[] opcoesJogadas = {"Pedra","Papel","Tesoura","Lagarto","Spock"};

    public static void main(String[] args) {
        try {
            //Define o Socket cliente
            Socket cliente = new Socket("127.0.0.1", 40001);
            PrintStream palpite = new PrintStream(cliente.getOutputStream());
            int rodada = 1;
            //Cria o jogo com duração de 15 rodadas
            while (rodada <= 15) {
                System.out.println("Rodada " + rodada);
                //Scanner que recebe as informações que o usuário insere pelo teclado
                Scanner entrada = new Scanner(System.in);
                if (rodada == 15) {
                    System.out.println("Ultima rodada");
                }
                //Escolha da opção inicial, ser aleatório ou o usuário escolher o palpite
                System.out.println("\n* Escolha uma opcao:\n 1- Palpite aleatorio\n 2- Informar um palpite\n 0- Para encerrar.\n -> Opcao: ");
                int opcao1 = entrada.nextInt();
                int opcao2 = -1;
                Random random = new Random();
                int index = random.nextInt(5);
                if (opcao1 == 1) {
                    //Envio do palpite aleatório e acréscimo de 1 em rodada
                    palpite.print(opcoesJogadas[index]);
                    rodada = rodada + 1;
                }
                if (opcao1 == 2) {
                    rodada = rodada + 1;
                    System.out.println("\n* Escolha o palpite:\n 1- Pedra\n 2- Papel\n 3- Tesoura\n 4- Lagarto\n 5- Spock\n -> Opcao: ");
                    opcao2 = entrada.nextInt();
                }
                //Envio do palpite desejado
                if (opcao2 == 1)
                    palpite.print("Pedra");
                else if (opcao2 == 2)
                    palpite.print("Papel");
                else if (opcao2 == 3)
                    palpite.print("Tesoura");
                else if (opcao2 == 4)
                    palpite.print("Lagarto");
                else if (opcao2 == 5)
                    palpite.print("Spock");

                if (opcao1 == 0) {
                    System.out.println("\nConexao encerrada!\n");
                    cliente.close();
                    break;
                }
                //Recebimento dos resultados da rodada
                BufferedReader in = new BufferedReader( new InputStreamReader(cliente.getInputStream()));
                //Printar na tela a mensagem recebida
                System.out.println(in.readLine());
                System.out.println(in.readLine());
                System.out.println(in.readLine());
                System.out.println();
            }
        }
        catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
