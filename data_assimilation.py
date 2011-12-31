from sympy import *
from sympy.stats import *

T = Normal(30,3)
print latex(P(T>33, evaluate=False))
print latex(P(T>33))
print latex(P(T>33).evalf())

noise = Normal(0, 1.5)
observation = T + noise

T_posterior = Given(T, Eq(observation, 26))

print latex(Density(T_posterior))
