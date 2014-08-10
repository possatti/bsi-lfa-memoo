Testa se o programa funciona da mesma forma, tanto para arquivos passados
por pipe, quanto para arquivos indicados pelas opções.

Os testes feitos aqui, são com exemplos retirados do livro.

Escreve os arquivos de teste.
  $ cat > book-mealy-to-moore.in << EOF
  > (mealy
  >   (symbols-in a1 ai an b)
  >   (symbols-out u1 ui un v)
  >   (states s q p)
  >   (start s)
  >   (finals p)
  >   (trans (s q a1 u1) (s q ai ui) (s q an un) (q p b v)))
  > EOF
  $ cat > book-moore-to-mealy.in << EOF
  > (moore
  >   (symbols-in a1 b1)
  >   (symbols-out u0 u1)
  >   (states q0 q1)
  >   (start q0)
  >   (finals q1)
  >   (trans (q0 q0 a0) (q0 q1 a1))
  >   (out-fn (q0 u0) (q1 u1)))
  > EOF

Testa a conversão de mealy para moore. Usando os dois métodos, para verificar
se eles gerão o mesmo resultado.
  $ $TESTDIR/../memoo.py < book-mealy-to-moore.in > book-mealy-to-moore.outstd
  $ $TESTDIR/../memoo.py -i book-mealy-to-moore.in -o book-mealy-to-moore.outfile
  $ diff -s book-mealy-to-moore.outstd book-mealy-to-moore.outfile
  Files book-mealy-to-moore.outstd and book-mealy-to-moore.outfile are identical

Testa a conversão de moore para mealy. Usando os dois métodos, para verificar
se eles gerão o mesmo resultado.
  $ $TESTDIR/../memoo.py < book-moore-to-mealy.in > book-moore-to-mealy.outstd
  $ $TESTDIR/../memoo.py -i book-moore-to-mealy.in -o book-moore-to-mealy.outfile
  $ diff -s book-moore-to-mealy.outstd book-moore-to-mealy.outfile
  Files book-moore-to-mealy.outstd and book-moore-to-mealy.outfile are identical
