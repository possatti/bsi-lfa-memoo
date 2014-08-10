  $ $TESTDIR/../memoo.py << EOF
  > (mealy
  >   (symbols-in a b)
  >   (symbols-out a b)
  >   (states q0 p0)
  >   (start q0)
  >   (finals p0)
  >   (trans
  >     (q0 p0 b b) (q0 q0 a a) (p0 q0 a a) (p0 p0 b ())))
  > EOF
  (moore (symbols-in a b) (symbols-out a b) (states q0 p0 p0*) (start q0) (finals p0 p0*) (trans (q0 p0 b) (q0 q0 a) (p0 q0 a) (p0 p0* b)) (out-fn (q0 a) (p0 b) (p0* ())))
  
