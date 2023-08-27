<p align="center">
    <img src="assets/logo_infnet.png" width="70" height="70" />
</p>

# Teste de Performance 1

## Exercício 8

Um poema simples consiste em quatro linhas. Cada linha consiste em uma ou mais palavras compostas por letras maiúsculas ou minúsculas, ou uma combinação de letras maiúsculas e minúsculas. Palavras adjacentes em uma linha são separadas por um único espaço.

Definimos a última sílaba de uma palavra (em Inglês) como a sequência de letras da última vogal ("a", "e", "i", "o" ou "u") até o final da palavra. Se uma palavra não tem vogal, então a última sílaba é a própria palavra. Dizemos que 2 linhas rimam se suas últimas sílabas forem iguais, ignorando maiúsculas e minúsculas.

Vocês devem classificar a forma de rima em um poema. A forma da rima pode ser perfeita, par, cruzada, concha ou livre:

- rima perfeita: as 4 linhas do poema rimam
- rima par: as 2 primeiras linhas rimam e as 2 últimas linhas rimam
- rima cruzada: a 1ª e a 3ª linhas rimam, assim como a 2ª e a 4ª
- rima concha: a 1ª e a 4ª linhas rimam, assim como a 2ª e a 3ª
- rima livre: qualquer forma que não seja perfeita, par, cruzada ou concha.

⚠️**Observação:** seu programa deve definir e usar funções apropriadas para a resolução do problema.

## Especificação da entrada
- 4 strings, as linhas do poema.

## Especificação da saída
- A forma de rima do poema (**perfeita**, **par**, **cruzada**, **concha** ou **livre**).

## Exemplos
| Entrada | Saída |
| ----------- | ----------- |
| One plus one is small<br>one hundred plus one is not<br>you might be very tall<br>but summer is not | cruzada |
| I say to you boo<br>You say boohoo<br>I cry too<br>It is too much foo | perfeita |
| Your teacher has to mark<br>and mark and mark and teach<br>To do well on this contest you have to reach<br>for everything with a lark | concha |
| It seems though<br>that without some dough<br>creating such a bash<br>is a weighty in terms of cash | par |
| But how I see<br>the problem so fair<br>is to write subtle verse<br>with hardly a rhyme | livre |