class A: pass
class B: pass
class C: pass
class D: pass
class E: pass            
class K1(A, B, C): pass    
class K2(D, B, E): pass    
class K3(D, A): pass    
class Z(K1, K2, K3): pass

print(Z.mro()) # [Z, K1, K2, K3, D, A, D, C, E, object]
