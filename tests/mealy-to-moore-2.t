  $ $TESTDIR/../memoo.py << EOF
  > (mealy
  >   (symbols-in a b)
  >   (symbols-out u v)
  >   (states q0 q1 q2)
  >   (start q0)
  >   (finals q2)
  >   (trans
  >     (q0 q1 a u) (q0 q2 b v) (q1 q2 a u) (q2 q1 b v)))
  > EOF
  (moore (symbols-in a b) (symbols-out u v) (states q0 q1 q1* q2 q2*) (start q0) (finals q2 q2*) (trans (q0 q1 a) (q0 q2 b) (q1 q2* a) (q2 q1* b)) (out-fn (q0 ()) (q1 u) (q1* v) (q2 v) (q2* u)))
