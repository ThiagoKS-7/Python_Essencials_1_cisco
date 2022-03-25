# Cenário 1
Era uma vez uma terra - uma terra de leite e mel, habitada por pessoas felizes e prósperas.
As pessoas pagavam impostos, claro - a sua felicidade tinha limites.
O imposto mais importante, denominado Imposto sobre o Rendimento das Pessoas Singulares
(IRS ou, em inglês, PIT), tinha de ser pago uma vez por ano, e foi avaliado utilizando a 
seguinte regra:

se o rendimento do cidadão não fosse superior a 85.528 thalers, o imposto era igual a 18% 
do rendimento menos 556 thalers e 2 cêntimos (este era o chamado desagravamento fiscal 
(em inglês, tax relief))
se o rendimento fosse superior a este montante, o imposto seria igual a 14.839 thalers e 2
 cêntimos, mais 32% do excedente acima de 85.528 thalers.
A sua tarefa é escrever uma calculadora de impostos.

Deve aceitar um valor de floating-point: o rendimento.
A seguir, deve imprimir o imposto calculado, arredondado a thalers completos. Há uma função
chamada round() que lhe fará o arredondamento por si - encontrá-la-á no código esqueleto no
editor.
Nota: este país feliz nunca devolve dinheiro aos seus cidadãos. Se o imposto
calculado for inferior a zero, significa apenas que não há qualquer imposto (o imposto é
igual a zero). Tenha isto em consideração durante os seus cálculos.

Veja o código no editor - lê apenas um valor de input e faz output de um resultado,
pelo que necessita de o completar com alguns cálculos inteligentes.


# Cenário 2
Como certamente sabe, devido a algumas razões astronómicas, os anos podem ser bissextos ou comuns. Os primeiros têm 366 dias de duração, enquanto os segundos têm 365 dias de duração.

Desde a introdução do calendário gregoriano (em 1582), a seguinte regra é utilizada para determinar o tipo de ano:

se o número do ano não for divisível por quatro, é um ano comum;
caso contrário, se o número do ano não for divisível por 100, é um ano bissexto;
caso contrário, se o número do ano não for divisível por 400, é um ano comum;
caso contrário, é um ano bissexto.
Veja o código no editor - lê apenas um número de ano, e precisa de ser completado com as instruções de implementação do teste que acabámos de descrever.

O código deve fazer output de uma de duas mensagens possíveis, que são Leap year ou Common year, dependendo do valor inserido.

Seria bom verificar se o ano introduzido cai na era Gregoriana, e faz output de um aviso caso contrário: Not within the Gregorian calendar period. Dica: use os operadores != e % .

