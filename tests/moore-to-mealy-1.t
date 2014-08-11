  $ $TESTDIR/../memoo.py << EOF
  > (moore
  >   (symbols-in a b)
  >   (symbols-out 0 1)
  >   (states q0 q1 q2 q3 q4 q5)
  >   (start q0)
  >   (finals q4 q5)
  >   (trans
  >     (q0 q2 a) (q0 q4 b) (q2 q5 a) (q2 q3 b)
  >     (q3 q1 a) (q3 q5 b) (q4 q5 a) (q4 q1 b)
  >     (q5 q5 a) (q5 q1 b))
  >   (out-fn
  >     (q0 ()) (q1 1) (q2 0)
  >     (q3 1) (q4 0) (q5 1)))
  > EOF
  (mealy (symbols-in a b) (symbols-out 0 1) (states qe q0 q1 q2 q3 q4 q5) (start qe) (finals q4 q5) (trans (qe q2 a 0) (q0 q2 a 0) (qe q4 b 0) (q0 q4 b 0) (q2 q5 a 1) (q2 q3 b 1) (q3 q1 a 1) (q3 q5 b 1) (q4 q5 a 1) (q4 q1 b 1) (q5 q5 a 1) (q5 q1 b 1)))
