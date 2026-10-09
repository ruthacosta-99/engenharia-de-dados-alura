# ☕ Sistema de Pedidos - Cafeteria Python

Projeto desenvolvido durante meus estudos de **Python para Dados**, com o objetivo de praticar estruturas condicionais e revisar conceitos estudados anteriormente.

O sistema simula o atendimento de uma cafeteria, realizando o cadastro de um pedido, aplicação de descontos, cálculo de entrega e verificação de benefícios para clientes.

## 🎯 Objetivo

Praticar principalmente o uso de:

- `if`
- `elif`
- `else`
- condições combinadas com `and`
- operadores de comparação
- cálculos com porcentagem

Além de revisar conceitos já estudados anteriormente em Python.

## ⚙️ Funcionalidades

O programa permite:

- cadastrar o nome e a idade do cliente;
- informar o produto escolhido;
- informar preço e quantidade;
- calcular o valor bruto da compra;
- verificar se o cliente participa do clube de fidelidade;
- aplicar diferentes descontos de acordo com o valor da compra;
- escolher entre retirada na loja ou entrega em domicílio;
- calcular o valor da entrega;
- calcular o valor final do pedido;
- verificar se o cliente ganhou um brinde;
- registrar uma observação sobre o pedido;
- manipular a observação utilizando métodos de strings.

## 💰 Regras de desconto

### Cliente do clube

| Valor da compra | Desconto |
|---|---:|
| Menor que R$ 50 | 5% |
| De R$ 50 até R$ 99,99 | 10% |
| R$ 100 ou mais | 15% |

### Cliente comum

| Valor da compra | Desconto |
|---|---:|
| Menor que R$ 50 | Sem desconto |
| De R$ 50 até R$ 99,99 | 5% |
| R$ 100 ou mais | 10% |

## 🚚 Regras de entrega

Para pedidos com entrega em domicílio:

| Valor bruto da compra | Frete |
|---|---:|
| Menor que R$ 50 | R$ 8,00 |
| De R$ 50 até R$ 99,99 | R$ 5,00 |
| R$ 100 ou mais | Grátis |

O valor utilizado para determinar o frete é o **valor bruto da compra, antes da aplicação do desconto**, para que o benefício do desconto não altere a faixa de entrega conquistada pelo cliente.

## 🍪 Brinde

Clientes que participam do clube de fidelidade e possuem valor da compra após o desconto igual ou superior a **R$ 80,00** recebem um cookie grátis.

## 🧠 Conceitos praticados

- Variáveis
- `input()`
- Conversão de tipos com `int()` e `float()`
- Operações matemáticas
- Cálculo de porcentagem
- `if`, `elif` e `else`
- Condições aninhadas
- Operador lógico `and`
- Operadores de comparação
- F-strings
- Formatação de valores decimais
- Métodos de strings:
  - `.upper()`
  - `.lower()`
  - `.strip()`

## 📚 Contexto

Este projeto faz parte dos meus estudos da formação de **Engenharia de Dados da Alura**.

Foi desenvolvido como exercício prático após o estudo de estruturas condicionais em Python, reunindo o novo conteúdo com conceitos vistos anteriormente.