# memoo

Programa simples feito em python para a conversão de máquinas de Mealy para máquinas de Moore e vice versa. O nome (memoo) vem das primeiras letras dos nomes Mealy e Moore. O código está hospedado nesse link: https://github.com/possatti/memoo

## Autor

Eu (Lucas Possatti) sou o autor de todo o código nesse projeto, com excessão do arquivo `sexp.py` na raiz do projeto, que usei para fazer o parsing das S-Expressions.

O código do arquivo `sexp.py` foi obitido [nesse link][http://rosettacode.org/wiki/S-Expressions#Python]. E fiz apenas algumas modificações nele. Apesar disso, não assumo qualquer crédito sobre esse código, e infelizmente no link eu não encontrei qualquer menção ao verdadeiro autor. Então deixo apenas o link.

Com excessão desse arquivo todo o resto do código é de minha autoria.

## Descrição do projeto

O projeto foi realizado como uma atividade da disciplina de Linguagens Formais e Automatos (LFA) do meu curso. O objetivo é criar um programa que leia uma definição de uma máquina de Mealy ou de Moore e converta para o seu oposto.

O projeto foi codificado inteiramente na linguagem Python 3. E apesar do código inteiro estar em inglês, ele está todo muito bem documentado em português.

As definições das máquinas de Moore e Mealy obedecem a sintaxe de S-Expressions. Eu não irei descrever aqui uma definição formal, mas você pode tomar os seguintes exemplos para entender como as máquinas devem ser definidas:

### Máquina de Moore

```lisp
(moore
  (symbols-in a b)
  (symbols-out 0 1)
  (states q0 q1 q2 q3 q4 q5)
  (start q0)
  (finals q4 q5)
  (trans
    (q0 q2 a) (q0 q4 b) (q2 q5 a) (q2 q3 b)
    (q3 q1 a) (q3 q5 b) (q4 q5 a) (q4 q1 b)
    (q5 q5 a) (q5 q1 b))
  (out-fn
    (q0 ()) (q1 1) (q2 0)
    (q3 1) (q4 0) (q5 1)))
```

### Máquina de Mealy

```lisp
(mealy
  (symbols-in a b)
  (symbols-out 0 1)
  (states q0 q1 q2 q3)
  (start q0)
  (finals q3)
  (trans
    (q0 q1 a 0) (q0 q3 b 0) (q1 q2 b 1) (q1 q3 a 1)
    (q2 q3 a 0) (q2 q3 b 1) (q3 q0 b 1) (q3 q3 a 1)))
```

*ATENÇÃO:* Quando você for definir uma máquina, você não deve usar asteriscos (*) para compor o nome dos estados, pois isso atrapalharia a convesão. Isso porque o asterisco é usado na criação de novos estados na conversão de Mealy para Moore. Portanto, não use estados que contenham o caracter asterisco no nome, pois o programa os usa internamente.

## Estrutura do projeto

O projeto se divide basicamente em três arquivos, são eles:
 - `memoo.py` : Programa principal. Este é o executável.
 - `converter.py` : Biblioteca com as rotinas de conversão das máquinas.
 - `sexp.py` : Biblioteca para leitura e escrita de S-Expressions.

Adicionalmente, na pasta `tests`, há um conjunto de testes que podem ser executados usando a framework [cram][https://bitheap.org/cram/]. Para utilizar a framework, é necessário instala-la previamente. Eu sugiro instala-la através do [pip][https://pypi.python.org/pypi/pip], que talvez já venha instalado na sua distribuição. Assim para instalar o `cram` é necessário um único comando:

```bash
$ sudo pip install cram
```

Para executar os testes, basta executar o `cram` indicando o diretório que contém os testes, da seguinte forma:

```bash
$ cram tests/
```

Também há uma pasta chamada `samples`, onde estão três exemplos de máquinas de Moore e três de Mealy. Inclusive, essas máquinas foram usadas como base para a elaboração dos testes.

## Modo de uso

O programa principal (memoo.py) é executado através da linha de comando, e deve ser interpretado usando um interpretador de Python 3.

Se o programa for executado sem qualquer argumento, ele lê o standard input em busca da S-Expression com a definição de uma máquina válida. E ao conseguir uma leitura válida, converte a máquina e escreve o resultado para o standard output.

Ou se o usuário preferir, é possível indicar arquivos para a leitura e saída através das seguintes opções:
 - -i FILE, --input FILE: Indica o local que contém a definição da máquina a ser convertida.
 - -o FILE, --output FILE: Indica o local onde a máquina convertida deverá ser escrita.

Assim, um exemplo de uma possível chamada ao programa é:

```bash
$ ./memoo.py -i input-machine.txt -o output-machine.txt
```

Também é possível ler um pequeno texto de ajuda através da opção `-h`.
