from sympy import *
from sympy.stats import *
X = Die(6)
Y = Die(6)
assert P(X>3) == S.Half
assert E(X+Y) == 7
assert E(2*X) == 7
assert Var(X+3) == S(35)/12
# assert Density(2*X) == {

density_map = {'heads': .5, 'tails':.5}
coin = FiniteRV(density_map)


