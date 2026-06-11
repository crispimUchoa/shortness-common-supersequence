# Shortest Common Supersequence

Implementação em Python para resolver o problema da **Shortest Common Supersequence** (SCS), ou **Menor Supersequência Comum**.

O objetivo do problema é, dadas duas strings, encontrar a menor string possível que contenha ambas como subsequências.

## Descrição do problema

Dadas duas strings `s1` e `s2`, deseja-se encontrar uma menor supersequência comum entre elas.

Uma string é considerada supersequência comum quando contém as duas strings originais como subsequências, mantendo a ordem dos caracteres.

### Exemplo

Entrada:

```txt
string1 string2
```

Uma possível saída:

```txt
string12
```

Nesse caso:

* `string1` é subsequência de `string12`
* `string2` é subsequência de `string12`

Logo, `string12` é uma supersequência comum das duas strings.

## Estratégia utilizada

A solução utiliza **Programação Dinâmica**, baseada na ideia da **Longest Common Subsequence** (LCS).

Primeiro, é construída uma tabela `dp` para encontrar os caracteres comuns entre as duas strings. Depois, essa tabela é percorrida de trás para frente para reconstruir a menor supersequência comum.

## Complexidade

Sejam:

* `n` o tamanho da primeira string
* `m` o tamanho da segunda string

A complexidade da solução é:

```txt
Tempo: O(n * m)
Memória: O(n * m)
```

## Estrutura do projeto

```txt
.
├── scs.py
├── messages.py
└── tests
    ├── test_0.txt
    ├── test_1.txt
    ├── test_2.txt
    ├── test_3.txt
    ├── test_4.txt
    └── test_5.txt
```

## Formato dos arquivos de teste

Cada arquivo de entrada deve conter duas strings separadas por espaço na primeira linha.

Formato esperado:

```txt
<string1> <string2>
```

Exemplo:

```txt
bleed blue
```

## Como executar

Para executar usando o arquivo padrão `./tests/test_0.txt`:

```bash
python scs.py
```

Para executar usando um arquivo específico:

```bash
python scs.py ./tests/test_1.txt
```

Para executar todos os arquivos de teste da pasta `./tests`:

```bash
python scs.py -a
```

ou:

```bash
python scs.py --all
```

Para exibir a mensagem de ajuda:

```bash
python scs.py -h
```

ou:

```bash
python scs.py --help
```

## Exemplos de entrada

### `test_0.txt`

```txt
bleed blue
```

### `test_1.txt`

```txt
cris rita
```

### `test_2.txt`

```txt
cirs rita
```

### `test_3.txt`

```txt
abab cab
```

### `test_4.txt`

```txt
abacaxi abacate
```

### `test_5.txt`

```txt
empreender microempreendedor
```

## Exemplo de saída

```txt
------------------ RESULTADOS ------------------
INPUTS:
String1: bleed
String2: blue

OUTPUTS:
Menor Supersequência: bleued
Tamanho: 6
------------------------------------------------
```

A saída apresenta:

* A primeira string de entrada
* A segunda string de entrada
* A menor supersequência encontrada
* O tamanho da supersequência

## Tratamento de erros

O programa trata alguns erros comuns, como:

* Arquivo não encontrado
* Formato de arquivo inválido
* Número excessivo de argumentos

Caso o arquivo não esteja no formato esperado, o programa informa que esperava duas strings separadas por espaço.

## Autor

Francisco Crispim Pinto Uchôa Neto

## Universidade

Universidade Estadual do Ceará — UECE

## Disciplina

Projeto e Análise de Algoritmos
