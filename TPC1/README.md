# TPC1: Somador on/off
- Data de entregue: 2025-02-14
- Nome: Luis Enrique Díaz De Freitas
- Número de Aluno: A104000




![Minha Foto](https://avatars.githubusercontent.com/u/146751915?s=400&u=021c640f21daf0066dc714d7cf1d916fefbd29ea&v=4)

## Enunciado
1. Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
2. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
3. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
4. Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

## Como funciona o programa?

Este projeto consiste no desenvolvimento de um programa capaz de ler um arquivo de texto e realizar a soma de números encontrados, respeitando comandos de ativação ("on") e desativação ("off"). Sempre que o comando "on" for identificado, os números subsequentes serão somados. Se o comando "off" aparecer, a soma será pausada até que "on" seja ativado novamente. O programa também reconhece o caractere "=" como um indicador para exibir a soma acumulada até aquele momento.

## Resultados obtidos

- somador_on_off.py – Código-fonte do programa.
- entrada.txt – Arquivo de entrada contendo os dados para processamento.