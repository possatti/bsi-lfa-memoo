  $ $TESTDIR/../memoo.py << EOF
  > (moore
  >   (symbols-in a b)
  >   (symbols-out 0 1)
  >   (states q0 q1 q1l)
  >   (start q0)
  >   (finals q1 q1l)
  >   (trans
  >     (q0 q1 a)
  >     (q0 q1 b)
  >     (q1 q0 a)
  >     (q1 q1l b)
  >     (q1l q1 a)
  >     (q1l q0 b))
  >   (out-fn
  >     (q0 ())
  >     (q1 0)
  >     (q1l 1)))
  > EOF
  (mealy (symbols-in a b) (symbols-out 0 1) (states qe q0 q1 q1l) (start qe) (finals q1 q1l) (trans (qe q1 a 0) (q0 q1 a 0) (qe q1 b 0) (q0 q1 b 0) (q1 q0 a ()) (q1 q1l b 1) (q1l q1 a 0) (q1l q0 b ())))
